merged = {}

for item in original:
    key = (item['price'], item['tickettypecode'], item['oneway'])
    if key in merged:
        for mergekey in ['inboundJourneys','outboundJourneys']:
            # assign extended copy rather than using list.extend()
            merged[key][mergekey] = merged[key][mergekey] + item[mergekey]
    else:
        merged[key] = item.copy()

mergedlist = merged.values()
