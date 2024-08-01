class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        mono_stack = []
        # preprocess
        time_to_target = []

        for i in range(len(position)):
            remaining_step = target - position[i]
            time = float(remaining_step) / speed[i]
            time_to_target.append(time)
        
        iterator = zip(position, speed, time_to_target)
        iterator.sort(key=lambda i: i[0])
        
        for pos, spd, time in iterator:
            # we only need to use time, and create a decreasing monotonic stack
            while len(mono_stack) > 0 and mono_stack[-1] <= time:
                mono_stack.pop()

            mono_stack.append(time)
        return len(mono_stack)
    
# Uses a decreasing monotonic stack. 
# We sort car by position, and also process how long it takes
# for the car to reach target
    
# For each car, if any of the car ahead reaches the target slower
# the current will join it to reach the final together