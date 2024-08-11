class Solution(object):
    def corpFlightBookings(self, bookings, n):
        answer = [0] * (n + 1)

        for firsti, lasti, seatsi in bookings:
            answer[firsti -1] += seatsi
            if lasti < n:
                answer[lasti] -= seatsi

        for i in range(1, n):
            answer[i] += answer[i - 1]

        return answer[:-1]            
