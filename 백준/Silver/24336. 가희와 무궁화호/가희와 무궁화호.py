n, q = map(int, input().split())
times = dict()
dist = {
    "Seoul": 0.0,
    "Yeongdeungpo": 9.1,
    "Anyang": 23.9,
    "Suwon": 41.5,
    "Osan": 56.5,
    "Seojeongri": 66.5,
    "Pyeongtaek": 75.0,
    "Seonghwan": 84.4,
    "Cheonan": 96.6,
    "Sojeongni": 107.4,
    "Jeonui": 114.9,
    "Jochiwon": 129.3,
    "Bugang": 139.8,
    "Sintanjin": 151.9,
    "Daejeon": 166.3,
    "Okcheon": 182.5,
    "Iwon": 190.8,
    "Jitan": 196.4,
    "Simcheon": 200.8,
    "Gakgye": 204.6,
    "Yeongdong": 211.6,
    "Hwanggan": 226.2,
    "Chupungnyeong": 234.7,
    "Gimcheon": 253.8,
    "Gumi": 276.7,
    "Sagok": 281.3,
    "Yangmok": 289.5,
    "Waegwan": 296.0,
    "Sindong": 305.9,
    "Daegu": 323.1,
    "Dongdaegu": 326.3,
    "Gyeongsan": 338.6,
    "Namseonghyeon": 353.1,
    "Cheongdo": 361.8,
    "Sangdong": 372.2,
    "Miryang": 381.6,
    "Samnangjin": 394.1,
    "Wondong": 403.2,
    "Mulgeum": 412.4,
    "Hwamyeong": 421.8,
    "Gupo": 425.2,
    "Sasang": 430.3,
    "Busan": 441.7,
}
start, end = '', ''
order = []
for i in range(n):
    city, arr, dep = input().split()
    if i == 0:
        start = city
        times[city] = [-1, int(dep[:2])*60 + int(dep[3:])]
    elif i == n-1:
        end = city
        times[city] = [int(arr[:2])*60 + int(arr[3:]), -1]
    else:
        times[city] = [int(arr[:2])*60 + int(arr[3:]), int(dep[:2])*60 + int(dep[3:])]
    order.append(city)

def calc(t1, t2):
    if t1 < t2: 
        return t2 - t1
    else:
        return 1440 - t1 + t2
    
for _ in range(q):
    c1, c2 = input().split()
    s, e = order.index(c1), order.index(c2)
    time = 0
    for i in range(s, e+1):
        if i!=s and i!=e:
            time += calc(times[order[i]][0], times[order[i]][1])
        if i != e:
            time += calc(times[order[i]][1], times[order[i+1]][0])
    d = abs(dist[c2] - dist[c1])
    print(d/time * 60)