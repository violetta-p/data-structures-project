"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(3, self.stack.top.data)
        self.assertEqual(2, self.stack.top.next_node.data)
        self.assertEqual(1, self.stack.top.next_node.next_node.data)
        self.assertEqual(None, self.stack.top.next_node.next_node.next_node)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(3, self.stack.pop())
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())
        self.assertEqual(None, self.stack.top)
