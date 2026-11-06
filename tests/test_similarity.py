import numpy as np
from scipy.sparse import csr_matrix

from pln.similarity import clasificar_por_prototipos, top_k_similares


def test_top_k_excluye_al_propio_documento():
    X = csr_matrix(np.array([[1, 0], [0.9, 0.1], [0, 1]]))
    idx, sims = top_k_similares(X, 0, k=2)
    assert 0 not in idx
    assert idx[0] == 1
    assert sims[0] >= sims[1]


def test_prototipos_asigna_la_clase_del_mas_similar():
    X_train = np.array([[1, 0], [0, 1]])
    y_train = ["a", "b"]
    X_test = np.array([[0.8, 0.2], [0.1, 0.9]])
    assert list(clasificar_por_prototipos(X_test, X_train, y_train)) == ["a", "b"]
