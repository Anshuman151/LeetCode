class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A = (ax2-ax1)*(ay2-ay1)
        B = (bx2-bx1)*(by2-by1)
        width_overlap = min(ax2,bx2) - max(ax1,bx1)
        height_overlap = min(ay2,by2) - max(ay1,by1)
        overlap = 0
        if width_overlap > 0 and height_overlap > 0:
            overlap = width_overlap*height_overlap
        total_area = A + B - overlap
        return total_area