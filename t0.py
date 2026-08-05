import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def average(scores):
    return sum(scores)/ len(scores)
def max_score(scores):
    return max(scores)
def min_score(scores):
    return min(scores)
students_scores= {
    "علی":[12,17,18],
    "مریم":[13,16,15],
    "مهسا":[11,20,15]
}
for name,scores in students_scores.items():
    avg=average(scores)

    max_s=max_score(scores)

    min_s=min_score(scores)
    
    print(f"{name} معدل:{avg:.2f} بالاترین نمره:{max_s} پایین ترین:{min_s}")
