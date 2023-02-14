current_hour, current_min, current_sec = map(int, input().split(':'))
throw_hour, throw_min, throw_sec = map(int, input().split(':'))

# 초로 변환해준다.
current_time = current_hour * 3600 + current_min * 60 + current_sec
throw_time = throw_hour * 3600 + throw_min * 60 + throw_sec

wait_time = 0

if throw_time > current_time:
    wait_time = throw_time - current_time
else:
    wait_time = throw_time - current_time + 24 * 3600

wait_hour = wait_time // 3600
wait_min = wait_time // 60 % 60
wait_sec = wait_time % 60

print("%02d:%02d:%02d" % (wait_hour, wait_min, wait_sec))