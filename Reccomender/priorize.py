#organize all data using a priority queue.
#python priortity queue uses a binary heap approach which has O(logn) operations
#this is a better approach than sorting an empty list. O(nlogn)

#priority queues are often used for scheduling

from queue import PriorityQueue
# python's priority queue is a min queue, so multiply everything by -1 to make it a max queue
def prioritize(score_dict):
    pq = PriorityQueue()
    for name,score in score_dict.items():
        pq.put((-score,name))
    return pq
