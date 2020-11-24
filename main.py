import numpy as np

a = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [9, 10, 11, 12, 13]])
hg = np.array([1,2,3,4,5,6,7,8,9,10], dtype = np.int64)
gh = np.array([2,4,3,6,7,5,1,8,9,10,56,47])
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
fg = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[1],[2],[3],[4],[5],[6],[7],[8],[9],[1],[2],[3],[4],[5],[6],[7],[8],[9]])
a2 = np.array([1,2,3,4,5,6])

print(a[2])
print(np.zeros(3))
print(np.ones(3, dtype = np.int64))
print(np.empty(3, dtype = np.int64))
print(np.arange(9))
print(np.arange(0,10,3))
print(np.linspace(0, 12.5, num=4))
print(np.sort(gh))
print("\n\n\n\n\n", np.argsort(a, axis=-1, kind=None, order=None))
print("\n\n\n\n\n", np.concatenate((hg, np.sort(gh))))
print("\n\n\n\n\n", np.concatenate((x, y), axis = 0))
print("\n\n\n\n\n", fg.ndim, fg.size, fg.shape)
print("\n\n\n\n\n", fg.reshape(3,3,3))
print("\n\n\n", np.reshape(a2, newshape=(1, 6), order='C'))