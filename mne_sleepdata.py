# https://mne.tools/stable/generated/mne.datasets.sleep_physionet.age.fetch_data.html

from mne.datasets.sleep_physionet.age import fetch_data

amount = 83

NAN_data = [39, 68, 69, 78, 79]
FAULT_data = {13: 1, 36: 2, 52: 2}

for i in range(amount):
    for j in [1, 2]:
        if i in NAN_data:
            pass

        if i in FAULT_data:
            pass
            # [data] = fetch_data(subjects=[i], recording=(FAULT_data[i]))
        else:
            [data] = fetch_data(subjects=[i], recording=[j])
