/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i;
    int j;
    int *new;

    new = malloc(sizeof(int) * 2);
    if (!new)
    return NULL;
    i = 0;

    while (i < numsSize)
    {
        j = 0;
        while (j < numsSize)
        {
            if (j == i)
            {
                j++;
            }
            if (nums[i] + nums[j] == target)
            {
                new[0] = i;
                new[1] = j;
                *returnSize = 2;
                return new;
            }
            j++;
        }
        i++;
    }
    return NULL;
}