#define FOR(a,b,c) for(a=b;a<c;a++)
bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    if(targetSize-arrSize)
        return false;
    int help[1001] = {0},index;
    FOR(index,0,targetSize)
        help[target[index]]++;
    FOR(index,0,arrSize)
        help[arr[index]]--;
    FOR(index,0,1001) if(help[index]) return false;
    return true;
}   
