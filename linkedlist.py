#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Any, Callable, Iterable, Iterator, Optional


class Node:
    """A single element of the list."""

    __slots__ = ("data", "next")

    def __init__(self, data: Any, nxt: Optional[Node] = None) -> None:
        self.data: Any = data
        self.next: Optional[Node] = nxt

    def __repr__(self) -> str:
        return f"Node({self.data!r})"


class LinkedList:
    """
    Singly-linked list exposing both iterative and recursive variants
    of the classic operations.
    """

    # -----------------------------------------------------------------
    # Construction / basic protocol
    # -----------------------------------------------------------------
    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """Create an empty list (or initialise from an iterable)."""
        self.head: Optional[Node] = None
        # optional: populate from `iterable` using push_back / push_back_recursive

    def __iter__(self) -> Iterator[Any]:
        """Yield the stored values (iterative traversal)."""
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __repr__(self) -> str:
        values = ", ".join(repr(v) for v in self)
        return f"LinkedList([{values}])"

    # -----------------------------------------------------------------
    # 1️⃣  Insertion
    # -----------------------------------------------------------------
    # Iterative front insertion
    def push_front(self, value: Any) -> None:
        """Insert `value` at the head (iterative)."""
        # raise NotImplementedError
        node = Node(value)
        node.next = self.head
        self.head = node

    # Iterative back insertion
    def push_back(self, value: Any) -> None:
        """Append `value` to the tail (iterative)."""
        # raise NotImplementedError
        snt = Node(None, self.head)
        tail = snt

        while tail.next:
            tail = tail.next

        tail.next = Node(value)

        self.head = snt.next

    # Recursive back insertion (public wrapper)
    def push_back_recursive(self, value: Any) -> None:
        """Append `value` to the tail (recursive)."""

        # raise NotImplementedError
        def _push_back_rec(node, value):
            if not node:
                return Node(value)

            node.next = _push_back_rec(node.next, value)

            return node

        self.head = _push_back_rec(self.head, value)

    # -----------------------------------------------------------------
    # 2️⃣  Deletion
    # -----------------------------------------------------------------
    def pop_front(self) -> Any:
        """Remove and return the head element (iterative)."""
        # raise NotImplementedError
        if not self.head:
            raise IndexError
            # return

        val = self.head.data
        self.head = self.head.next

        return val

    def delete(self, value: Any) -> bool:
        """Delete first node equal to `value` (iterative). Return True if removed."""
        # raise NotImplementedError
        snt = Node(None, self.head)
        tail = snt
        found = False

        while tail.next:
            if tail.next.data == value:
                tail.next = tail.next.next
                found = True
                break
            tail = tail.next

        self.head = snt.next
        return found

    def delete_recursive(self, value: Any) -> bool:
        """Delete first node equal to `value` (recursive). Return True if removed."""

        # raise NotImplementedError
        def _delete_rec(node, value):
            if not node:
                return None, False

            if node.data == value:
                return node.next, True

            node.next, found = _delete_rec(node.next, value)

            return node, found

        self.head, found = _delete_rec(self.head, value)
        return found

    # -----------------------------------------------------------------
    # 3️⃣  Search
    # -----------------------------------------------------------------
    def find(self, value: Any) -> Optional[Node]:
        """Return the first node containing `value` (iterative)."""
        # raise NotImplementedError
        curr = self.head
        while curr:
            if curr.data == value:
                return curr
            curr = curr.next

        return None

    def find_recursive(self, value: Any) -> Optional[Node]:
        """Return the first node containing `value` (recursive)."""
        # raise NotImplementedError

        def _find_rec(node):
            if not node:
                return node

            if node.data == value:
                return node

            return _find_rec(node.next)

        return _find_rec(self.head)

    # -----------------------------------------------------------------
    # 4️⃣  Size / Length
    # -----------------------------------------------------------------
    def __len__(self) -> int:
        """Return the number of elements (iterative)."""
        # raise NotImplementedError
        ln = 0

        curr = self.head

        while curr:
            curr = curr.next
            ln += 1

        return ln

    def length_recursive(self) -> int:
        """Return the number of elements (recursive)."""

        # raise NotImplementedError
        def _len_rec(node):
            if not node:
                return 0

            return 1 + _len_rec(node.next)

        return _len_rec(self.head)

    # -----------------------------------------------------------------
    # 5️⃣  Reverse
    # -----------------------------------------------------------------
    def reverse(self) -> None:
        """Reverse the list in-place (iterative)."""
        # raise NotImplementedError
        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    def reverse_recursive(self) -> None:
        """Reverse the list in-place (recursive)."""

        # raise NotImplementedError
        def _reverse_rec(node, prev):
            if not node:
                return prev

            nxt = node.next
            node.next = prev

            return _reverse_rec(nxt, node)

        self.head = _reverse_rec(self.head, None)

    # -----------------------------------------------------------------
    # 6️⃣  Apply a function to each element
    # -----------------------------------------------------------------
    def apply(self, func: Callable[[Any], Any]) -> None:
        """Apply `func` to every node's data (iterative)."""
        # raise NotImplementedError
        curr = self.head
        while curr:
            curr.data = func(curr.data)
            curr = curr.next

    def apply_recursive(self, func: Callable[[Any], Any]) -> None:
        """Apply `func` to every node's data (recursive)."""

        # raise NotImplementedError
        def _apply_rec(node):
            if not node:
                return

            node.data = func(node.data)

            _apply_rec(node.next)

        _apply_rec(self.head)

    # -----------------------------------------------------------------
    # 7️⃣  Helper methods (private)
    # -----------------------------------------------------------------
    # Recursive helpers can be placed here, e.g.:
    #   def _push_back_rec(self, node: Optional[Node], value: Any) -> Node: ...
    #   def _delete_rec(self, node: Optional[Node], value: Any) -> Optional[Node]: ...
    #   def _find_rec(self, node: Optional[Node], value: Any) -> Optional[Node]: ...
    #   def _len_rec(self, node: Optional[Node]) -> int: ...
    #   def _reverse_rec(self, node: Optional[Node]) -> Optional[Node]: ...
    #   def _apply_rec(self, node: Optional[Node], func: Callable[[Any], Any]) -> None: ...
    pass  # (placeholder – replace with actual methods when you implement)


# -------------------------------------------------------------------------
# Example of how the API would be used (no concrete logic yet)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    lst = LinkedList()
    lst.push_front(1)
    lst.push_back(2)
    lst.push_back_recursive(3)

    print(lst)  # LinkedList([...]) – depends on future __repr__
    print(len(lst))  # size
    lst.reverse()
    lst.reverse_recursive()
    node = lst.find(2)
    lst.apply(lambda x: x * 2)
    lst.apply_recursive(lambda x: -x)
