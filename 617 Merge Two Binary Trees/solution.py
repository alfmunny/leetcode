# 1. Recursive solution
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution1(object):
  def mergeTrees(self, t1, t2):
    if not t1:
      return t2
    if not t2:
      return t1

    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t2.right = self.mergeTrees(t1.right, t2.right)

    return t1


# 2. Iterative solution. Inorder traverse

class Solution2(object):
	def mergeTrees(self, t1, t2):
			if not t1:
					return t2

			stack = [[t1, t2]]

			while(stack):
					t = stack.pop()

					if (not t[0] or not t[1]):
							continue

					t[0].val += t[1].val

					if not t[0].left:
							t[0].left = t[1].left
					else:
							stack.append([t[0].left, t[1].left])

					if not t[0].right:
							t[0].right = t[1].right
					else:
							stack.append([t[0].right, t[1].right])
			return t1










