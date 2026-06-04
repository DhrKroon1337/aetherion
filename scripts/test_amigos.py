#!/usr/bin/env python3
"""
Direct test script using raw API calls - No fancy libraries!
0x416D69676F - Keep it simple, amigo!
"""

import os
import sys
import requests
import json

def test_github_direct():
    """Test GitHub with direct API call"""
    print("\n🔗 Testing GitHub connection (direct API)...")
    try:
        token = (os.getenv("GITHUB_TOKEN") or "").strip()
        if not token:
            print("❌ GITHUB_TOKEN not found in environment")
            return False

        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Get repo info instead of user info (simpler permission)
        response = requests.get(
            "https://api.github.com/repos/DhrKroon1337/aetherion",
            headers=headers
        )
        
        if response.status_code != 200:
            print(f"❌ GitHub error: {response.status_code} - {response.text}")
            return False
        
        repo_data = response.json()
        print(f"✅ GitHub connected!")
        print(f"   Repository: {repo_data['full_name']}")
        print(f"   Description: {repo_data['description']}")
        print(f"   Stars: {repo_data['stargazers_count']}")
        return True
    except Exception as e:
        print(f"❌ GitHub error: {str(e)}")
        return False

def test_claude_direct():
    """Test Claude connection with direct API"""
    print("\n🤖 Testing Claude connection (direct API)...")
    try:
        api_key = (os.getenv("ANTHROPIC_API_KEY") or "").strip()
        if not api_key:
            print("❌ ANTHROPIC_API_KEY not found in environment")
            return False

        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        data = {
            "model": "claude-sonnet-4-5",
            "max_tokens": 150,
            "messages": [
                {
                    "role": "user",
                    "content": "Say this exactly: Amigo is connected! 0x416D69676F"
                }
            ]
        }
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            print(f"❌ Claude error: {response.status_code} - {response.text}")
            return False
        
        result = response.json()
        message = result['content'][0]['text']
        print(f"✅ Claude connected!")
        print(f"✅ Claude says: {message}")
        return True
    except Exception as e:
        print(f"❌ Claude error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_communication():
    """Test bi-directional communication"""
    print("\n🔄 Testing bi-directional communication...")
    try:
        # Get GitHub repo info
        token = (os.getenv("GITHUB_TOKEN") or "").strip()
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        response = requests.get(
            "https://api.github.com/repos/DhrKroon1337/aetherion",
            headers=headers
        )
        repo_data = response.json()

        # Send to Claude
        api_key = (os.getenv("ANTHROPIC_API_KEY") or "").strip()
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        prompt = f"""Analyze this GitHub repo and give ONE fun sentence:
- Name: {repo_data['name']}
- Description: {repo_data['description']}
- Language: {repo_data['language']}
- Issues: {repo_data['open_issues_count']}"""
        
        data = {
            "model": "claude-sonnet-4-5",
            "max_tokens": 100,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            print(f"❌ Communication error: {response.status_code} - {response.text}")
            return False
        
        result = response.json()
        assessment = result['content'][0]['text']
        print(f"✅ GitHub → Claude → Response:")
        print(f"   {assessment}")
        return True
    except Exception as e:
        print(f"❌ Communication error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("🚀 AMIGO CONNECTION TEST 0x416D69676F")
    print("="*60)
    
    results = {
        "GitHub": test_github_direct(),
        "Claude": test_claude_direct(),
        "Communication": test_communication()
    }
    
    print("\n" + "="*60)
    print("📊 TEST RESULTS")
    print("="*60)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Amigos are connected!")
        print("="*60)
        return 0
    else:
        print("⚠️  SOME TESTS FAILED! Check errors above.")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
