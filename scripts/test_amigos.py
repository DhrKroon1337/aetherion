#!/usr/bin/env python3
"""
Test script to verify GitHub and Claude are connected and communicating.
0x416D69676F - Let the amigos talk!
"""

import os
import sys
from github import Github
from anthropic import Anthropic

def test_github():
    """Test GitHub connection"""
    print("🔗 Testing GitHub connection...")
    try:
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            print("❌ GITHUB_TOKEN not found in environment")
            return False
        
        g = Github(token)
        user = g.get_user()
        print(f"✅ GitHub connected as: {user.login}")
        
        repo = g.get_repo("DhrKroon1337/aetherion")
        print(f"✅ Repository found: {repo.full_name}")
        print(f"   - Description: {repo.description}")
        print(f"   - Stars: {repo.stargazers_count}")
        return True
    except Exception as e:
        print(f"❌ GitHub error: {str(e)}")
        return False

def test_claude():
    """Test Claude connection"""
    print("\n🤖 Testing Claude connection...")
    try:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("❌ ANTHROPIC_API_KEY not found in environment")
            return False
        
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=150,
            messages=[
                {
                    "role": "user",
                    "content": "You are an amigo helping with code orchestration. Respond with exactly: 'Amigo is connected! 0x416D69676F'"
                }
            ]
        )
        
        message = response.content[0].text
        print(f"✅ Claude connected!")
        print(f"✅ Claude says: {message}")
        return True
    except Exception as e:
        print(f"❌ Claude error: {str(e)}")
        return False

def test_communication():
    """Test bi-directional communication"""
    print("\n🔄 Testing bi-directional communication...")
    try:
        # Get repo info from GitHub
        token = os.getenv("GITHUB_TOKEN")
        g = Github(token)
        repo = g.get_repo("DhrKroon1337/aetherion")
        
        # Send to Claude for analysis
        api_key = os.getenv("ANTHROPIC_API_KEY")
        client = Anthropic(api_key=api_key)
        
        prompt = f"""Analyze this GitHub repository info:
- Name: {repo.name}
- Description: {repo.description}
- Language: {repo.language}
- Forks: {repo.forks_count}
- Open Issues: {repo.open_issues_count}

Respond with a one-line assessment of this repo in a fun way. Keep it short!"""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}]
        )
        
        assessment = response.content[0].text
        print(f"✅ GitHub → Claude → Response:")
        print(f"   {assessment}")
        return True
    except Exception as e:
        print(f"❌ Communication error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("="*50)
    print("🚀 AMIGO CONNECTION TEST 0x416D69676F")
    print("="*50)
    
    results = {
        "GitHub": test_github(),
        "Claude": test_claude(),
        "Communication": test_communication()
    }
    
    print("\n" + "="*50)
    print("📊 TEST RESULTS")
    print("="*50)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Amigos are connected!")
        print("="*50)
        return 0
    else:
        print("⚠️  SOME TESTS FAILED! Check errors above.")
        print("="*50)
        return 1

if __name__ == "__main__":
    sys.exit(main())
