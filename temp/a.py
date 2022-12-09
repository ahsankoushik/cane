import os

a = os.system(f'''espeak "The Boeing 747 is a large, long-range wide-body airliner designed and manufactured by Boeing Commercial Airplanes in the United States. After introducing the 707 in October 1958" 2>/dev/null''')


print(a)
print('ok')