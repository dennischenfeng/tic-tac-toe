"""
Unit tests for tic_tac_toe
"""

import pytest
from tic_tac_toe.tic_tac_toe import Engine


@pytest.fixture
def engine():
    return Engine()


def test_play_move(engine):
    s = engine.play_move(0, 0)
    assert s
    assert engine.board == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

    s = engine.play_move(1, 0)
    assert s
    assert engine.board == [[1, 0, 0], [2, 0, 0], [0, 0, 0]]

    s = engine.play_move(2, 2)
    assert s
    assert engine.board == [[1, 0, 0], [2, 0, 0], [0, 0, 1]]


def test_play_move_invalid(engine):
    s = engine.play_move(-1, 0)
    assert not s
    assert engine.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    s = engine.play_move(0, 0)
    assert s
    assert engine.board == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

    s = engine.play_move(0, 0)
    assert not s
    assert engine.board == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_display_board(engine):
    engine.play_move(1, 1)
    engine.play_move(2, 0)
    engine.play_move(0, 0)
    d = engine.visual_board()
    assert d == [["X", " ", " "], [" ", "X", " "], ["O", " ", " "]]


def test_compute_game_status_player1(engine):
    engine.play_move(0, 0)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 0)
    assert engine.compute_game_status() == 0
    engine.play_move(0, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(0, 2)
    assert engine.compute_game_status() == 1


def test_compute_game_status_player2(engine):
    engine.play_move(1, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 0)
    assert engine.compute_game_status() == 0
    engine.play_move(0, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(0, 2)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 2)
    assert engine.compute_game_status() == 2


def test_compute_game_status_draw(engine):
    engine.play_move(0, 0)
    assert engine.compute_game_status() == 0
    engine.play_move(0, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(0, 2)
    assert engine.compute_game_status() == 0
    engine.play_move(1, 1)
    assert engine.compute_game_status() == 0
    engine.play_move(1, 0)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 0)
    assert engine.compute_game_status() == 0
    engine.play_move(1, 2)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 2)
    assert engine.compute_game_status() == 0
    engine.play_move(2, 1)
    assert engine.compute_game_status() == 3

