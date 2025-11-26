from abc import ABC, abstractmethod
class SortingStrategy(ABC):
@abstractmethod
def sort(self, array):
pass
class BubbleSortStrategy(SortingStrategy):
def sort(self, array):
print('Sorting using Bubble Sort')
# Bubble sort implementation
class MergeSortStrategy(SortingStrategy):
def sort(self, array):
print('Sorting using Merge Sort')
# Merge sort implementation
class QuickSortStrategy(SortingStrategy):
def sort(self, array):
print('Sorting using Quick Sort')
# Quick sort implementation
class SortingContext:
def __init__(self, strategy):
self.strategy = strategy
def perform_sort(self, array):
self.strategy.sort(array)
def set_sorting_strategy(self, strategy):
self.strategy = strategy
# Create SortingContext with BubbleSortStrategy
sorting_context = SortingContext(BubbleSortStrategy())
array1 = ['cpp','c','java','python3','csharp','html','css','javascript','php','cpp14','cobol','dart','go','julia','kotlin','lisp','matlab','node','objc','perl','r','rust','ruby','scala','swift','solidity','xml']
sorting_context.perform_sort(array1) # Output: Sorting using Bubble Sort
# Change strategy to MergeSortStrategy
sorting_context.set_sorting_strategy(MergeSortStrategy())
array2 = ['cpp','c','java','python3','csharp','html','css','javascript','php','cpp14','cobol','dart','go','julia','kotlin','lisp','matlab','node','objc','perl','r','rust','ruby','scala','swift','solidity','xml']
sorting_context.perform_sort(array2) # Output: Sorting using Merge Sort
# Change strategy to QuickSortStrategy
sorting_context.set_sorting_strategy(QuickSortStrategy())
array3 = ['cpp','c','java','python3','csharp','html','css','javascript','php','cpp14','cobol','dart','go','julia','kotlin','lisp','matlab','node','objc','perl','r','rust','ruby','scala','swift','solidity','xml']
sorting_context.perform_sort(array3) # Output: Sorting using Quick Sort