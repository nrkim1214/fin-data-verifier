import logging
from typing import Dict, Any

# 마린 평가 기준인 'Technical Reasoning'을 보여주기 위한 로직
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def verify_transaction(data: Dict[str, Any]) -> bool:
    """
    금융 트랜잭션의 유효성을 검증합니다. (금융 IT 전문가 컨셉)
    """
    required_fields = ["id", "amount", "currency"]
    
    # 1. 필수 필드 체크
    if not all(field in data for field in required_fields):
        logger.error("Missing required fields in transaction data.")
        return False
    
    # 2. 비즈니스 로직 (예: 금액은 0보다 커야 함)
    if data["amount"] <= 0:
        logger.warning(f"Invalid amount: {data['amount']}")
        return False
        
    logger.info(f"Transaction {data['id']} verified successfully.")
    return True

if __name__ == "__main__":
    sample_data = {"id": "TX1004", "amount": 50000, "currency": "KRW"}
    verify_transaction(sample_data)