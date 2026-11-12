"""清点分区冻结边界，不判断事务可见记录。"""
from .io import integer

def summarize(v,root):
    seen=set()
    for p in v['partitions']:
        key=(p['topic_uuid'],integer(p['partition']))
        if key in seen:raise ValueError('分区重复')
        seen.add(key)
        if not integer(p['log_start'])<=integer(p['start'])<=integer(p['lso'])<=integer(p['high_watermark']):raise ValueError('日志边界逆序')
        integer(p['leader_epoch'])
    return {'partitions':len(seen),'recorded_calls':len(v['steps']),'sum_frozen_span':sum(p['lso']-p['start'] for p in v['partitions'])}
