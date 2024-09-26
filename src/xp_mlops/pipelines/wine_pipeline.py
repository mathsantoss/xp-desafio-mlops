
import pickle
import pandas as pd
from kedro.pipeline import node, Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

def load_data():
    """Carrega o dataset Wine diretamente do sklearn."""
    wine_data = load_wine()
    # Cria um DataFrame com os dados
    df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)
    df['target'] = wine_data.target  # Adiciona a coluna de alvo
    return df

def split_data(data, target='target', test_size=0.2, random_state=42):
    """Divide os dados em conjuntos de treino e teste."""
    X = data.drop(columns=[target])  # Remove a coluna alvo para X
    y = data[target]  # A coluna alvo para y
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    """Treina um modelo Random Forest com os dados de treino."""
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo com o conjunto de teste e retorna a acurácia."""
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

def save_model(model, filepath):
    """Salva o modelo treinado em um arquivo."""
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=load_data,
            inputs=None,  # Não precisa de inputs, pois carrega o dataset diretamente
            outputs="wine_data",
            name="load_data_node"
        ),
        node(
            func=split_data,
            inputs=["wine_data", "params:target"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node"
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="model",
            name="train_model_node"
        ),
        node(
            func=evaluate_model,
            inputs=["model", "X_test", "y_test"],
            outputs="accuracy",
            name="evaluate_model_node"
        ),
        node(
            func=save_model,
            inputs=["model", "params:model_save_path"],
            outputs=None,  # Não há saída, apenas salva o modelo
            name="save_model_node"
        )
    ])
