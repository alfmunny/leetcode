class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        oldColor = image[sr][sc]
        stack = []
        if newColor != oldColor:
            stack.append([sr, sc])

        m = len(image)
        n = len(image[0])

        while stack:
            p = stack.pop()
            x, y = p

            image[x][y] = newColor

            for v in [[1, 0], [0, 1]]:
                for s in [1, -1]:
                    r = v[0] * s
                    c = v[1] * s
                    if 0 <= x + r < m and 0 <= y + c < n and image[x + r][y + c] == oldColor:
                        stack.append([x + r, y + c])

        return image
