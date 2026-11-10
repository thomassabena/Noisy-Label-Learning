# Learning with Noisy Labels: Data Efficiency Study

Machine Learning course project (COSC 522), University of Tennessee, Knoxville.

## Overview

Image classification datasets can contain incorrect labels. In this group project, we investigated whether the relative performance of methods for learning with noisy labels changes as the available training set gets smaller.

The team compared five approaches (ProMix, PLS, CAL, ELR, and T-Revision) on CIFAR-10N and CIFAR-100N, using 10%, 20%, 30%, 50%, 70%, and 100% of the training data. The wider comparison was collaborative, while my assigned method was **CAL (Calibrated Loss)**.

## My Contribution: CAL

Starting from the original [UCSC-REAL/CAL](https://github.com/UCSC-REAL/CAL) implementation, I worked on:

- **Experimental setup:** Modified the training scripts to introduce a `dataset_size` parameter for experiments with different training-data fractions (10%, 20%, 30%, 50%, 70%, and 100%).
- **Training configuration:** Adjusted training parameters for CIFAR-10N and CIFAR-100N, including the number of epochs.
- **Performance evaluation:** Collected and analyzed classification accuracy across different training-data sizes.
- **Comparative analysis:** Contributed the CAL results to the team's comparison of five noisy-label learning algorithms.

The underlying CAL algorithm was developed by the original authors and was not modified.

## CAL results

The following results were recorded during the course project.
Accuracy generally improved as more training data became available.

| Training data | CIFAR-10N | CIFAR-100N |
| ---: | ---: | ---: |
| 10% | 41.90% | 16.60% |
| 20% | 73.25% | 27.65% |
| 30% | 76.90% | 39.00% |
| 50% | 84.18% | 48.22% |
| 70% | 86.21% | 56.31% |
| 100% | 90.15% | 61.71% |

![CAL accuracy by training data fraction](results/cal_accuracy.png)

The values above come from the original course results spreadsheet, not newly executed experiments. The CSV in `results/` also includes the recorded clean-label comparisons, and the original spreadsheet is retained for reference.

## Repository contents

- `experiments/` — saved CIFAR-10 and CIFAR-100 CAL experiment scripts, adapted from upstream code
- `analysis/` — script for inspecting compatible training logs
- `results/` — original results workbook, derived CSV, and accuracy plot

## Code

The experimental scripts are adapted from the original [UCSC-REAL/CAL](https://github.com/UCSC-REAL/CAL) implementation.

The repository contains the saved experiment configurations, analysis tools, and recorded results. The original CAL framework and datasets are available from their respective sources.

## License and Attribution

The CAL implementation is based on the original
[UCSC-REAL/CAL](https://github.com/UCSC-REAL/CAL) repository, released under the MIT License.

The original copyright and license notice are preserved in `LICENSE-UPSTREAM`.

## References and credits

- [CIFAR-N datasets and benchmark](https://www.yliuu.com/web-cifarN/index.html); see also [noisylabels.com](http://noisylabels.com/)
- [UCSC-REAL/CAL source code](https://github.com/UCSC-REAL/CAL) — original implementation, distributed under the MIT license. The upstream copyright and permission notice is included as `LICENSE-UPSTREAM`.
- Zhu, Z., Liu, T., and Liu, Y. (2021). *A Second-Order Approach to Learning with Instance-Dependent Label Noise*. CVPR. [Paper](https://arxiv.org/abs/2012.11854).
- Wei, J., Zhu, Z., Cheng, H., Liu, T., Niu, G., and Liu, Y. (2022). *Learning with Noisy Labels Revisited: A Study Using Real-World Human Annotations*. ICLR. [Paper](https://openreview.net/forum?id=TBWA6PLJZQm).

Group project collaborators: Cem Ege Ergun, Todd Casey Van Meter, Khan A. Yawar, and Adam Winschel. The five-algorithm comparison and presentation were team work. 
This repository focuses on my CAL experiments only.
