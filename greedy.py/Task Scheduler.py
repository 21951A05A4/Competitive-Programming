class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count=Counter(tasks)
        max_freq=max(task_count.values())
        max_freq_tasks=sum(1 for count in task_count.values() if count==max_freq)
        interval_needed=(max_freq-1)*(n+1)+max_freq_tasks
        return max(interval_needed,len(tasks))
