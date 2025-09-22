#!/usr/bin/env python3
import requests
import os
import datetime

def get_github_contributions():
    # This is a simplified version - GitHub's actual contribution data requires GraphQL
    # For now, we'll create a mock SVG that looks like the real one
    
    # You would need to implement actual GitHub API calls here
    # Using GitHub's GraphQL API to get contribution data
    
    return {
        'current_streak': 7,
        'longest_streak': 15, 
        'total_contributions': 284,
        'this_year_contributions': 127
    }

def generate_streak_svg():
    data = get_github_contributions()
    
    svg_content = f'''
<svg width="100%" height="180" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#ff6d00;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#ff9e00;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <style>
        .card {{
            fill: #0d1117;
            stroke: #30363d;
            stroke-width: 1;
            rx: 10;
        }}
        .title {{
            fill: #f0f6fc;
            font-family: 'Segoe UI', Ubuntu, sans-serif;
            font-size: 16px;
            font-weight: 600;
        }}
        .streak-number {{
            fill: url(#gradient);
            font-family: 'Segoe UI', Ubuntu, sans-serif;
            font-size: 32px;
            font-weight: 700;
        }}
        .label {{
            fill: #8b949e;
            font-family: 'Segoe UI', Ubuntu, sans-serif;
            font-size: 12px;
        }}
        .stat-number {{
            fill: #f0f6fc;
            font-family: 'Segoe UI', Ubuntu, sans-serif;
            font-size: 20px;
            font-weight: 600;
        }}
        .footer {{
            fill: #8b949e;
            font-family: 'Segoe UI', Ubuntu, sans-serif;
            font-size: 10px;
        }}
    </style>
    
    <!-- Background Card -->
    <rect width="100%" height="100%" class="card"/>
    
    <!-- Title -->
    <text x="50%" y="30" text-anchor="middle" class="title">GitHub Streak Stats</text>
    
    <!-- Current Streak -->
    <text x="50%" y="80" text-anchor="middle" class="streak-number">{data['current_streak]} days</text>
    <text x="50%" y="100" text-anchor="middle" class="label">Current Streak</text>
    
    <!-- Stats Row -->
    <g transform="translate(0, 120)">
        <!-- Longest Streak -->
        <text x="25%" y="0" text-anchor="middle" class="stat-number">{data['longest_streak]}</text>
        <text x="25%" y="15" text-anchor="middle" class="label">Longest</text>
        
        <!-- Total Contributions -->
        <text x="50%" y="0" text-anchor="middle" class="stat-number">{data['total_contributions]}</text>
        <text x="50%" y="15" text-anchor="middle" class="label">Total</text>
        
        <!-- This Year -->
        <text x="75%" y="0" text-anchor="middle" class="stat-number">{data['this_year_contributions]}</text>
        <text x="75%" y="15" text-anchor="middle" class="label">This Year</text>
    </g>
    
    <!-- Footer -->
    <text x="50%" y="170" text-anchor="middle" class="footer">Updated: {datetime.datetime.now().strftime("%Y-%m-%d")}</text>
</svg>
'''.strip()
    
    with open('streak.svg', 'w') as f:
        f.write(svg_content)
    print("Advanced streak SVG generated!")

if __name__ == "__main__":
    generate_streak_svg()
