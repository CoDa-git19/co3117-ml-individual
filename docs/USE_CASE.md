# Use Case (2026-09-27)

## 1. Dataset and version
UCI Human Activity Recognition Using Smartphones (UCI ID 240,
"UCI HAR Dataset", 2012 release). 30 subjects, 10299 windows.
Download procedure and checksum: see data/README.md.

## 2. Target variable
Six mutually exclusive activity classes: WALKING,
WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING.
Multi-class classification. Frozen for the whole semester; no
relabelling and no class merging.

## 3. Decision context
Recognise the physical activity of a person wearing a
waist-mounted smartphone, from inertial sensor readings alone.
Errors are not symmetric in practice: confusing two static
postures (SITTING vs STANDING) matters less than confusing a
static posture with locomotion, so per-class performance is
reported alongside the aggregate metric.

## 4. Sealed test set
The 9 subjects in the original test/ directory (2947 windows).
Held out entirely; touched once per model, after hyperparameters
are fixed on validation. See docs/PROTOCOL.md.

## 5. Primary representation
The 561 pre-extracted time- and frequency-domain features supplied
by the dataset authors, computed over 2.56-second sliding windows
with 50% overlap. Known limitation: these features were normalised
to [-1, 1] over the whole dataset before the train/test split;
this is documented in docs/PROTOCOL.md and is not removable
without discarding the feature set.

## 6. Planned alternative representation (Part II)
Sequence models in Part II (HMM) cannot use the 561-feature table,
because that table discards the temporal ordering of windows.
For those models I will build a sequence representation from the
Inertial Signals/ directory of the SAME raw dataset: 9 channels of
128-sample windows at 50 Hz, reassembled into per-subject sequences
using the subject and activity label files.
