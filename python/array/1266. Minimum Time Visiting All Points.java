package array;
class Solution{
    public int minTimeToVisitAllPoints(int[][] points){
        int dist = 0;
        for (int i = 0; i < points.length - 1; i++){
            int a = Math.abs(points[i][0] - points[i + 1][0]);
            int b = Math.abs(points[i][1] - points[i + 1][1]);
            if (a < b){
                dist = dist + b;
            }else if (b <a){
                dist = dist + a;
            }
            else{
                dist = dist + a;
            }
        }
        return dist;
    }
}