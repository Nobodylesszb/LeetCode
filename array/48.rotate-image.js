var rotate = function(matrix) {
    const oMatrix = JSON.parse(JSON.stringify(matrix));
    const n = oMatrix.length;
    for (let i =0;i<N;i++){
        for (let j =0;j<n;j++){
            matrix[j][n-i-1] = oMatrix[i][j]; 
        }
    }
}