def solution(id_list, report, k):
    report_table = {callee_id: set() for callee_id in id_list}
    for info in report:
        caller, callee = info.split()
        report_table[callee].add(caller)
    
    answer = [0] * len(id_list)
    for callee in report_table:
        if len(report_table[callee]) >= k:
            for i, caller in enumerate(id_list):
                if caller in report_table[callee]:
                    answer[i] += 1
    return answer
