# 2446 - Troco (Programação Dinâmica)
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2446


def dp(coins: list[int], target: int) -> bool:
    solutions = [False] * (target + 1)
    
    # De graça é sempre possível
    solutions[0] = True

    for c in coins:
        for i in range(target, c - 1, -1):
            # Se existe solução para `i - c`,
            # Então existe solução para `i`
            if solutions[i - c]:
                solutions[i] = True

    return solutions[target]


if __name__ == '__main__':
    target, _ = map(int, input().split())
    coins = map(int, input().split())

    print('S' if dp(coins, target) else 'N')
   
