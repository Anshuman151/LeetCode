class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A = (ax2-ax1)*(ay2-ay1)
        B = (bx2-bx1)*(by2-by1)
        #width of overlap
        left = max(ax1,bx1)
        right = min(ax2,bx2)
        width_overlap = right - left
        #height of overlap
        top = min(ay2,by2)
        bottom = max(ay1,by1)
        height_overlap = top - bottom
        #area of overlap
        overlap = 0
        if width_overlap > 0 and height_overlap > 0:
            overlap = width_overlap*height_overlap
        #total area
        total_area = A + B - overlap
        return total_area