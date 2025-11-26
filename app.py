import sys

def decimal_to_binary_8bit(number):
    """
    10진수를 8비트 2진수 문자열로 변환합니다.
    (0~255 범위를 벗어나면 오류를 반환)
    """
    if not 0 <= number <= 255:
        return f"오류: 입력값 {number}는 0부터 255 사이여야 합니다.", False
    
    # '08b' 포맷을 사용하여 8자리 2진수(b)로 변환하고, 부족한 자리는 0으로 채웁니다.
    binary_str = format(number, '08b')
    return binary_str, True

def perform_bit_operations(num1, num2):
    """
    두 10진수에 대해 AND, OR, XOR 연산을 수행하고 결과를 딕셔너리로 반환합니다.
    """
    results = {}
    
    # 파이썬의 비트 연산자: & (AND), | (OR), ^ (XOR)
    operations = [
        ("AND", num1 & num2),
        ("OR", num1 | num2),
        ("XOR", num1 ^ num2)
    ]
    
    for op_name, dec_result in operations:
        # 연산 결과를 다시 8비트 2진수로 변환
        bin_result = format(dec_result, '08b')
        results[op_name] = {'dec': dec_result, 'bin': bin_result}
        
    return results

def main():
    """프로그램의 메인 실행 로직"""
    print("==============================================")
    print("✨ 8비트 이진수 변환 및 비트 연산 시뮬레이터")
    print("==============================================")
    
    try:
        # 입력 단계
        num_a = int(input(">> 첫 번째 10진수 (A) 입력 (0~255): "))
        num_b = int(input(">> 두 번째 10진수 (B) 입력 (0~255): "))
        
    except ValueError:
        print("\n[❌ 오류] 숫자가 아닌 값을 입력했습니다. 프로그램을 종료합니다.")
        sys.exit(1)

    # 1. 변환 및 유효성 검사
    bin_a, valid_a = decimal_to_binary_8bit(num_a)
    bin_b, valid_b = decimal_to_binary_8bit(num_b)
    
    if not (valid_a and valid_b):
        # 유효성 검사 실패 시, decimal_to_binary_8bit 함수에서 반환된 오류 메시지 출력
        print(f"\n[❌ 오류] {bin_a if not valid_a else bin_b}")
        sys.exit(1)

    print("\n--- 1. 이진수 변환 결과 (8비트) ---")
    print(f"A ({num_a:3d}) -> 2진수: {bin_a}")
    print(f"B ({num_b:3d}) -> 2진수: {bin_b}")
    
    # 2. 비트 연산 수행
    results = perform_bit_operations(num_a, num_b)
    
    print("\n--- 2. 비트 논리 연산 결과 (A, B) ---")
    
    # 결과 출력 (AND, OR, XOR)
    for op_name, data in results.items():
        print(f"\n[A {op_name} B]")
        print(f"   A:  {bin_a}")
        print(f" {op_name}: {bin_b}")
        print("   --------------------")
        print(f"결과: {data['bin']}  (10진수: {data['dec']})")

if __name__ == "__main__":
    main()
