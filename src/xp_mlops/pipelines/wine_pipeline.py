import pickle
import pandas as pd
from kedro.pipeline import node, Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import os
from sklearn.datasets import load_wine


def load_data():
    """
    Carrega o dataset de vinho.
    """
    data = load_wine()
    X = data.data[:, 1:]  # Remove a coluna 'alcohol' (primeira)
    y = data.data[:, 0]  # O target será o teor alcoólico
    return X, y


def split_data(X, y, test_size: float, random_state: int):
    """
    Divide os dados em conjuntos de treino e teste.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train):
    """Treina um modelo Random Forest com os dados de treino."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def predict_and_evaluate(model, X_test, y_test):
    """
    Faz previsões e avalia o modelo.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse, y_pred


def save_model(model, filepath):
    """Salva o modelo treinado em um arquivo."""
    with open(filepath, "wb") as f:
        pickle.dump(model, f)


def create_model_directory(filepath):
    """Cria o diretório para salvar o modelo se ele não existir."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_data,
                inputs=None,
                outputs=["X", "y"],
                name="load_data_node",
            ),
            node(
                func=split_data,
                inputs=["X", "y", "params:test_size", "params:random_state"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="model",
                name="train_model_node",
            ),
            node(
                func=predict_and_evaluate,
                inputs=["model", "X_test", "y_test"],
                outputs=["mse", "y_pred"],
                name="predict_and_evaluate_node",
            ),
            node(
                func=create_model_directory,
                inputs=["params:model_save_path"],
                outputs=None,
                name="create_model_directory_node",
            ),
            node(
                func=save_model,
                inputs=["model", "params:model_save_path"],
                outputs=None,  # Não há saída, apenas salva o modelo
                name="save_model_node",
            ),
        ]
    )
