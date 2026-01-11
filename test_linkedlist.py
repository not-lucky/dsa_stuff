#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unittest suite for the LinkedList implementation that skips tests
where the exercised method is still a stub (raises NotImplementedError).

Place the implementation (Node + LinkedList) in a file called
`linkedlist.py` in the same directory as this test file.
"""

import unittest
from typing import List

# ----------------------------------------------------------------------
# Import the implementation
# ----------------------------------------------------------------------
from linkedlist import LinkedList  # <-- your skeleton file


# ----------------------------------------------------------------------
# Helper utilities
# ----------------------------------------------------------------------
def as_list(ll: LinkedList) -> List:
    """Convert a LinkedList into a plain Python list."""
    return list(ll)


def assert_contents(testcase: unittest.TestCase, ll: LinkedList, expected: List):
    """Assert that `ll` holds exactly the items in `expected`."""
    testcase.assertEqual(as_list(ll), expected)


# ----------------------------------------------------------------------
# Helper to wrap a call that may raise NotImplementedError
# ----------------------------------------------------------------------
def safe_call(testcase: unittest.TestCase, func, *args, **kwargs):
    """
    Execute *func* with the supplied arguments.
    If the function raises NotImplementedError the current test
    is skipped with a helpful message.
    """
    try:
        return func(*args, **kwargs)
    except NotImplementedError as exc:
        testcase.skipTest(f"{func.__name__} not implemented: {exc}")


# ----------------------------------------------------------------------
# Basic tests – empty list and one‑element list
# ----------------------------------------------------------------------
class TestLinkedListBasics(unittest.TestCase):
    def setUp(self):
        self.empty = LinkedList()
        self.singleton = LinkedList()
        safe_call(self, self.singleton.push_front, 42)

    # --------------------------------------------------------------
    # Insertion
    # --------------------------------------------------------------
    def test_push_front(self):
        ll = LinkedList()
        safe_call(self, ll.push_front, "a")
        assert_contents(self, ll, ["a"])

        safe_call(self, ll.push_front, "b")
        assert_contents(self, ll, ["b", "a"])

    def test_push_back_iterative(self):
        ll = LinkedList()
        safe_call(self, ll.push_back, 10)
        assert_contents(self, ll, [10])

        safe_call(self, ll.push_back, 20)
        safe_call(self, ll.push_back, 30)
        assert_contents(self, ll, [10, 20, 30])

    def test_push_back_recursive(self):
        ll = LinkedList()
        safe_call(self, ll.push_back_recursive, "x")
        assert_contents(self, ll, ["x"])

        safe_call(self, ll.push_back_recursive, "y")
        safe_call(self, ll.push_back_recursive, "z")
        assert_contents(self, ll, ["x", "y", "z"])

    # --------------------------------------------------------------
    # Deletion / pop_front
    # --------------------------------------------------------------
    def test_pop_front_empty(self):
        with self.assertRaises(IndexError):
            safe_call(self, self.empty.pop_front)

    def test_pop_front_normal(self):
        ll = LinkedList()
        safe_call(self, ll.push_front, 1)
        safe_call(self, ll.push_front, 2)  # 2 → 1

        val = safe_call(self, ll.pop_front)
        self.assertEqual(val, 2)
        assert_contents(self, ll, [1])

        # pop last element
        val = safe_call(self, ll.pop_front)
        self.assertEqual(val, 1)
        assert_contents(self, ll, [])

    # --------------------------------------------------------------
    # Length
    # --------------------------------------------------------------
    def test_len_builtin(self):
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(self.singleton), 1)

        multi = LinkedList()
        for v in (4, 3, 2, 1):
            safe_call(self, multi.push_front, v)  # builds 1 → 2 → 3 → 4
        self.assertEqual(len(multi), 4)

    def test_length_recursive(self):
        self.assertEqual(self.empty.length_recursive(), 0)
        self.assertEqual(self.singleton.length_recursive(), 1)

        multi = LinkedList()
        for v in (4, 3, 2, 1):
            safe_call(self, multi.push_front, v)
        self.assertEqual(multi.length_recursive(), 4)

    # --------------------------------------------------------------
    # Reverse
    # --------------------------------------------------------------
    def test_reverse_empty(self):
        safe_call(self, self.empty.reverse)
        assert_contents(self, self.empty, [])

        safe_call(self, self.empty.reverse_recursive)
        assert_contents(self, self.empty, [])

    def test_reverse_singleton(self):
        safe_call(self, self.singleton.reverse)
        assert_contents(self, self.singleton, [42])

        safe_call(self, self.singleton.reverse_recursive)
        assert_contents(self, self.singleton, [42])

    # --------------------------------------------------------------
    # Apply (in‑place transformation)
    # --------------------------------------------------------------
    def test_apply_empty(self):
        safe_call(self, self.empty.apply, lambda x: x * 2)
        assert_contents(self, self.empty, [])

        safe_call(self, self.empty.apply_recursive, lambda x: x * 2)
        assert_contents(self, self.empty, [])


# ----------------------------------------------------------------------
# Advanced tests – list with several elements
# ----------------------------------------------------------------------
class TestLinkedListAdvanced(unittest.TestCase):
    def setUp(self):
        # Build a list 1 → 2 → 3 → 4
        self.ll = LinkedList()
        for v in (4, 3, 2, 1):
            safe_call(self, self.ll.push_front, v)

    # --------------------------------------------------------------
    # Find / search
    # --------------------------------------------------------------
    def test_find_iterative(self):
        for val, idx in [(1, 0), (2, 1), (3, 2), (4, 3), (999, None)]:
            node = safe_call(self, self.ll.find, val)
            if idx is None:
                self.assertIsNone(node)
            else:
                cur = self.ll.head
                for _ in range(idx):
                    cur = cur.next  # type: ignore[assignment]
                self.assertIs(node, cur)
                self.assertEqual(node.data, val)

    def test_find_recursive(self):
        for val, idx in [(1, 0), (2, 1), (3, 2), (4, 3), (999, None)]:
            node = safe_call(self, self.ll.find_recursive, val)
            if idx is None:
                self.assertIsNone(node)
            else:
                cur = self.ll.head
                for _ in range(idx):
                    cur = cur.next  # type: ignore[assignment]
                self.assertIs(node, cur)
                self.assertEqual(node.data, val)

    # --------------------------------------------------------------
    # Delete – iterative vs recursive
    # --------------------------------------------------------------
    def test_delete_iterative(self):
        # delete head
        removed = safe_call(self, self.ll.delete, 1)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [2, 3, 4])

        # delete middle
        removed = safe_call(self, self.ll.delete, 3)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [2, 4])

        # delete tail
        removed = safe_call(self, self.ll.delete, 4)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [2])

        # delete non‑existent
        removed = safe_call(self, self.ll.delete, 999)
        self.assertFalse(removed)
        assert_contents(self, self.ll, [2])

    def test_delete_recursive(self):
        # reset list to original state
        self.setUp()

        # delete head
        removed = safe_call(self, self.ll.delete_recursive, 1)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [2, 3, 4])

        # delete middle
        removed = safe_call(self, self.ll.delete_recursive, 3)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [2, 4])

        # delete tail
        removed = safe_call(self, self.ll.delete_recursive, 4)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [2])

        # delete non‑existent
        removed = safe_call(self, self.ll.delete_recursive, 999)
        self.assertFalse(removed)
        assert_contents(self, self.ll, [2])

    # --------------------------------------------------------------
    # Reverse – iterative vs recursive, idempotence
    # --------------------------------------------------------------
    def test_reverse_iterative(self):
        safe_call(self, self.ll.reverse)
        assert_contents(self, self.ll, [4, 3, 2, 1])

    def test_reverse_recursive(self):
        safe_call(self, self.ll.reverse_recursive)
        assert_contents(self, self.ll, [4, 3, 2, 1])

    def test_reverse_twice_returns_original(self):
        original = as_list(self.ll)
        safe_call(self, self.ll.reverse)
        safe_call(self, self.ll.reverse)
        self.assertEqual(as_list(self.ll), original)

    def test_reverse_iter_vs_rec(self):
        # make independent copies
        it = LinkedList()
        for v in as_list(self.ll):
            safe_call(self, it.push_back, v)

        rec = LinkedList()
        for v in as_list(self.ll):
            safe_call(self, rec.push_back, v)

        safe_call(self, it.reverse)
        safe_call(self, rec.reverse_recursive)
        self.assertEqual(as_list(it), as_list(rec))

    # --------------------------------------------------------------
    # Apply – iterative vs recursive
    # --------------------------------------------------------------
    def test_apply_iterative(self):
        safe_call(self, self.ll.apply, lambda x: x * 2)
        assert_contents(self, self.ll, [2, 4, 6, 8])

    def test_apply_recursive(self):
        safe_call(self, self.ll.apply_recursive, lambda x: -x)
        assert_contents(self, self.ll, [-1, -2, -3, -4])

    # --------------------------------------------------------------
    # Mixed operations (stress test)
    # --------------------------------------------------------------
    def test_mixed_workflow(self):
        ll = LinkedList()
        safe_call(self, ll.push_back, 1)  # 1
        safe_call(self, ll.push_front, 0)  # 0 → 1
        safe_call(self, ll.push_back_recursive, 2)  # 0 → 1 → 2
        safe_call(self, ll.push_front, -1)  # -1 → 0 → 1 → 2
        assert_contents(self, ll, [-1, 0, 1, 2])

        safe_call(self, ll.delete, 0)
        assert_contents(self, ll, [-1, 1, 2])

        safe_call(self, ll.reverse_recursive)
        assert_contents(self, ll, [2, 1, -1])

        safe_call(self, ll.apply, lambda x: x * 10)
        assert_contents(self, ll, [20, 10, -10])

        self.assertEqual(safe_call(self, ll.pop_front), 20)
        self.assertEqual(safe_call(self, ll.pop_front), 10)
        self.assertEqual(safe_call(self, ll.pop_front), -10)
        assert_contents(self, ll, [])

        self.assertEqual(len(ll), 0)
        safe_call(self, ll.reverse)  # should stay empty, no exception
        assert_contents(self, ll, [])


# ----------------------------------------------------------------------
# Entry point – run the suite when the file is executed directly
# ----------------------------------------------------------------------

class TestLinkedListComprehensive(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    # --------------------------------------------------------------
    # Duplicate handling
    # --------------------------------------------------------------
    def test_find_duplicate_values(self):
        # Setup: 1 -> 2 -> 2 -> 3
        safe_call(self, self.ll.push_back, 1)
        safe_call(self, self.ll.push_back, 2)
        safe_call(self, self.ll.push_back, 2)
        safe_call(self, self.ll.push_back, 3)

        # Test iterative find
        node1 = safe_call(self, self.ll.find, 2)
        self.assertIsNotNone(node1)
        self.assertEqual(node1.data, 2)
        # Verify it's the first occurrence (next should be the second 2)
        # Note: We rely on structure here. If find returned the second one, next would be 3.
        self.assertEqual(node1.next.data, 2)
        self.assertEqual(node1.next.next.data, 3)

        # Test recursive find
        node2 = safe_call(self, self.ll.find_recursive, 2)
        self.assertIsNotNone(node2)
        self.assertEqual(node2.data, 2)
        # Should find the exact same node object
        self.assertIs(node2, node1)

    def test_delete_duplicate_values(self):
        # Setup: 1 -> 2 -> 2 -> 3
        safe_call(self, self.ll.push_back, 1)
        safe_call(self, self.ll.push_back, 2)
        safe_call(self, self.ll.push_back, 2)
        safe_call(self, self.ll.push_back, 3)

        # Delete first 2
        removed = safe_call(self, self.ll.delete, 2)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [1, 2, 3])

        # Delete remaining 2
        removed = safe_call(self, self.ll.delete, 2)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [1, 3])

    def test_delete_recursive_duplicate_values(self):
        # Setup: 1 -> 2 -> 2 -> 3
        safe_call(self, self.ll.push_back, 1)
        safe_call(self, self.ll.push_back, 2)
        safe_call(self, self.ll.push_back, 2)
        safe_call(self, self.ll.push_back, 3)

        # Delete first 2
        removed = safe_call(self, self.ll.delete_recursive, 2)
        self.assertTrue(removed)
        assert_contents(self, self.ll, [1, 2, 3])

    # --------------------------------------------------------------
    # Repr
    # --------------------------------------------------------------
    def test_repr(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        # Based on implementation: return f"LinkedList([{values}])"
        # and Node repr: f"Node({self.data!r})"
        # But LinkedList __iter__ yields data, not nodes.
        # __repr__ implementation: values = ", ".join(repr(v) for v in self)
        # so it prints repr of data.
        self.assertEqual(repr(self.ll), "LinkedList([1, 2])")

    def test_node_repr(self):
        # We need to access Node class or create a node indirectly
        # Since Node is not imported, we can get it from the list
        self.ll.push_back("test")
        node = self.ll.head
        self.assertEqual(repr(node), "Node('test')")

    # --------------------------------------------------------------
    # Mixed types
    # --------------------------------------------------------------
    def test_mixed_types(self):
        safe_call(self, self.ll.push_back, 1)
        safe_call(self, self.ll.push_back, "string")
        safe_call(self, self.ll.push_back, [1, 2])

        assert_contents(self, self.ll, [1, "string", [1, 2]])

        # Test finding mixed types
        node = safe_call(self, self.ll.find, "string")
        self.assertEqual(node.data, "string")

        node = safe_call(self, self.ll.find, [1, 2])
        self.assertEqual(node.data, [1, 2])

        # Test deleting mixed types
        safe_call(self, self.ll.delete, "string")
        assert_contents(self, self.ll, [1, [1, 2]])


    # --------------------------------------------------------------
    # Stress tests
    # --------------------------------------------------------------
    def test_large_list_iterative(self):
        # 2000 items should be fine for iterative
        n = 2000
        for i in range(n):
            safe_call(self, self.ll.push_back, i)

        self.assertEqual(len(self.ll), n)
        safe_call(self, self.ll.reverse)
        if self.ll.head:
            self.assertEqual(self.ll.head.data, n - 1)

        # Iterative delete from end
        safe_call(self, self.ll.delete, 0)
        self.assertEqual(len(self.ll), n - 1)

    def test_recursive_limit_safe(self):
        # 300 items should be safe for recursion (limit is 1000)
        # We use a smaller number to avoid hitting the limit on some platforms/implementations
        n = 300
        for i in range(n):
            safe_call(self, self.ll.push_back, i)

        # Test recursive length
        try:
            length = self.ll.length_recursive()
            self.assertEqual(length, n)
        except RecursionError:
            self.fail("RecursionError raised for list size 300")
        except NotImplementedError:
            pass

        # Test recursive reverse
        try:
            self.ll.reverse_recursive()
            if self.ll.head:
                self.assertEqual(self.ll.head.data, n - 1)
        except RecursionError:
            self.fail("RecursionError raised for list size 300")
        except NotImplementedError:
            pass

if __name__ == "__main__":
    unittest.main()
