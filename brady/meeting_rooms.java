/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
  
    // O(nlgn) time, O(1) space
    public boolean canAttendMeetings(List<Interval> intervals) {
        Collections.sort(intervals, (i1, i2) -> {
            return i2.start - i1.start;
        });

        for (int i = 0; i < intervals.size()-1; ++i) {
            if (intervals.get(i).end > intervals.get(i+1).start) return false;
        }

        return true;
    }
}
