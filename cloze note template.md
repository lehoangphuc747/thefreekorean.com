<!DOCTYPE html>

<html lang="vi">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Ngữ pháp Tiếng Hàn: 밖에</title>

    <!-- Import Noto Sans KR for Korean text and Roboto for Vietnamese -->

    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">

    <style>

        :root {

            --primary-color: #3498db;

            --secondary-color: #2c3e50;

            --accent-color: #e74c3c;

            --bg-color: #f4f7f6;

            --card-bg: #ffffff;

            --success-color: #2ecc71;

            --text-color: #333;

            --text-light: #666;

            --shadow: 0 4px 6px rgba(0, 0, 0, 0.05);

            --radius: 12px;

        }

  

        * {

            box-sizing: border-box;

            margin: 0;

            padding: 0;

        }

  

        body {

            font-family: 'Roboto', sans-serif;

            background-color: var(--bg-color);

            color: var(--text-color);

            line-height: 1.6;

        }

  

        .container {

            max-width: 800px;

            margin: 0 auto;

            padding: 20px;

        }

  

        /* HEADER */

        header {

            text-align: center;

            margin-bottom: 40px;

            padding: 40px 20px;

            background: linear-gradient(135deg, #3498db, #8e44ad);

            color: white;

            border-radius: 0 0 20px 20px;

            box-shadow: var(--shadow);

        }

  

        .brand {

            font-size: 0.9rem;

            letter-spacing: 2px;

            opacity: 0.9;

            text-transform: uppercase;

            margin-bottom: 10px;

            display: block;

        }

  

        h1 {

            font-size: 3rem;

            margin-bottom: 10px;

            font-family: 'Noto Sans KR', sans-serif;

        }

  

        .subtitle {

            font-size: 1.2rem;

            opacity: 0.9;

        }

  

        /* CARD STYLE */

        .card {

            background: var(--card-bg);

            border-radius: var(--radius);

            padding: 25px;

            margin-bottom: 25px;

            box-shadow: var(--shadow);

            border-left: 5px solid var(--primary-color);

        }

  

        .card h2 {

            font-size: 1.4rem;

            color: var(--secondary-color);

            margin-bottom: 20px;

            display: flex;

            align-items: center;

            gap: 10px;

            border-bottom: 1px solid #eee;

            padding-bottom: 10px;

        }

  

        /* FORMULA BOX */

        .formula-box {

            background-color: #e8f4fd;

            padding: 20px;

            border-radius: 8px;

            text-align: center;

            font-size: 1.3rem;

            font-weight: bold;

            color: var(--secondary-color);

            margin: 15px 0;

            border: 2px dashed var(--primary-color);

        }

  

        .korean-highlight {

            color: var(--primary-color);

            font-family: 'Noto Sans KR', sans-serif;

        }

  

        .negative-highlight {

            color: var(--accent-color);

        }

  

        /* EXAMPLES GRID */

        .example-grid {

            display: grid;

            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));

            gap: 15px;

        }

  

        .example-item {

            background: #fafafa;

            padding: 15px;

            border-radius: 8px;

            border: 1px solid #eee;

            transition: transform 0.2s;

        }

  

        .example-item:hover {

            transform: translateY(-2px);

            border-color: var(--primary-color);

        }

  

        .kr-sent {

            font-family: 'Noto Sans KR', sans-serif;

            font-size: 1.15rem;

            font-weight: 700;

            color: var(--secondary-color);

            margin-bottom: 5px;

            display: block;

        }

  

        .vi-mean {

            font-size: 0.95rem;

            color: var(--text-light);

        }

  

        /* COMPARISON TABLE */

        .comparison-table {

            width: 100%;

            border-collapse: collapse;

            margin-top: 10px;

        }

  

        .comparison-table th, .comparison-table td {

            padding: 12px;

            border-bottom: 1px solid #eee;

            text-align: left;

        }

  

        .comparison-table th {

            background-color: #f8f9fa;

            color: var(--secondary-color);

        }

  

        /* WRONG/RIGHT EXAMPLES */

        .check-list {

            list-style: none;

        }

  

        .check-item {

            margin-bottom: 15px;

            padding: 10px;

            border-radius: 6px;

        }

  

        .check-item.wrong {

            background-color: #fff5f5;

            border-left: 4px solid var(--accent-color);

        }

  

        .check-item.right {

            background-color: #f0fcf4;

            border-left: 4px solid var(--success-color);

        }

  

        .badge {

            display: inline-block;

            padding: 2px 6px;

            border-radius: 4px;

            font-size: 0.8rem;

            font-weight: bold;

            margin-right: 8px;

        }

  

        .badge.x { background: var(--accent-color); color: white; }

        .badge.o { background: var(--success-color); color: white; }

  

        /* FOOTER */

        footer {

            text-align: center;

            padding: 20px;

            color: var(--text-light);

            font-size: 0.9rem;

            margin-top: 40px;

        }

  

        /* Responsive adjustments */

        @media (max-width: 600px) {

            h1 { font-size: 2.2rem; }

            .container { padding: 10px; }

            .card { padding: 15px; }

            .example-grid { grid-template-columns: 1fr; }

        }

    </style>

</head>

<body>

  

    <header>

        <span class="brand">The Free Korean</span>

        <h1>밖에</h1>

        <div class="subtitle">Chỉ... thôi / Ngoài ra không còn</div>

    </header>

  

    <div class="container">

  

        <!-- 1. Core Logic -->

        <section class="card">

            <h2>🌟 Tư duy cốt lõi</h2>

            <div class="formula-box">

                <span class="korean-highlight">Danh từ</span> +

                <span class="korean-highlight">밖에</span> +

                <span class="negative-highlight">Phủ định</span>

            </div>

            <p><strong>Quy tắc vàng:</strong></p>

            <ul style="margin-left: 20px; margin-top: 10px;">

                <li>Nhấn mạnh rằng <strong>ngoài cái này ra thì không còn cái nào khác</strong>.</li>

                <li>Phía sau <strong>BẮT BUỘC</strong> phải là câu phủ định:<br>

                    <span class="korean-highlight">없다</span> (không có), <span class="korean-highlight">안</span> (không), <span class="korean-highlight">못</span> (không thể), <span class="korean-highlight">모르다</span> (không biết).

                </li>

            </ul>

        </section>

  

        <!-- 2. Examples Section -->

        <section class="card">

            <h2>🗣️ Ví dụ thực tế</h2>

            <p style="margin-bottom: 15px; color: #666;">Di chuột vào thẻ để xem rõ hơn.</p>

            <div class="example-grid">

                <!-- Item 1 -->

                <div class="example-item">

                    <span class="kr-sent">돈이 천 원<span class="korean-highlight">밖에</span> <span class="negative-highlight">없어요</span>.</span>

                    <span class="vi-mean">Tôi chỉ có đúng 1000 won (ngoài ra không còn).</span>

                </div>

                <!-- Item 2 -->

                <div class="example-item">

                    <span class="kr-sent">3명<span class="korean-highlight">밖에</span> <span class="negative-highlight">없어요</span>.</span>

                    <span class="vi-mean">Chỉ có 3 người thôi.</span>

                </div>

                <!-- Item 3 -->

                <div class="example-item">

                    <span class="kr-sent">가방 안에 책<span class="korean-highlight">밖에</span> <span class="negative-highlight">없어요</span>.</span>

                    <span class="vi-mean">Trong cặp chỉ có mỗi sách (không có gì khác).</span>

                </div>

                <!-- Item 4 -->

                <div class="example-item">

                    <span class="kr-sent">한국어<span class="korean-highlight">밖에</span> <span class="negative-highlight">몰라요</span>.</span>

                    <span class="vi-mean">Tôi chỉ biết tiếng Hàn (không biết tiếng khác).</span>

                </div>

                 <!-- Item 5 -->

                 <div class="example-item">

                    <span class="kr-sent">조금<span class="korean-highlight">밖에</span> <span class="negative-highlight">못</span> 했어요.</span>

                    <span class="vi-mean">Tôi chỉ làm được một chút thôi.</span>

                </div>

                <!-- Item 6 -->

                <div class="example-item">

                    <span class="kr-sent">너<span class="korean-highlight">밖에</span> <span class="negative-highlight">몰라요</span>.</span>

                    <span class="vi-mean">Anh chỉ biết mỗi em thôi.</span>

                </div>

            </div>

        </section>

  

        <!-- 3. Common Mistakes -->

        <section class="card" style="border-left-color: var(--accent-color);">

            <h2>🚫 Lưu ý quan trọng (Hay sai)</h2>

            <ul class="check-list">

                <li class="check-item wrong">

                    <span class="badge x">SAI</span>

                    <span class="kr-sent">돈이 천 원밖에 <strong>있어요</strong>.</span>

                    <div class="vi-mean">Sai vì đuôi câu là khẳng định.</div>

                </li>

                <li class="check-item right">

                    <span class="badge o">ĐÚNG</span>

                    <span class="kr-sent">돈이 천 원밖에 <strong>없어요</strong>.</span>

                    <div class="vi-mean">Phải dùng phủ định (없다).</div>

                </li>

                <hr style="border: 0; border-top: 1px dashed #ddd; margin: 10px 0;">

                <li class="check-item wrong">

                    <span class="badge x">SAI</span>

                    <span class="kr-sent">이것밖에 <strong>드세요</strong>.</span>

                    <div class="vi-mean">Sai vì dùng mệnh lệnh (Hãy ăn...).</div>

                </li>

                <li class="check-item right">

                    <span class="badge o">ĐÚNG</span>

                    <span class="kr-sent">이것<strong>만</strong> 드세요.</span>

                    <div class="vi-mean">Câu mệnh lệnh phải dùng "만".</div>

                </li>

            </ul>

        </section>

  

        <!-- 4. Comparison -->

        <section class="card">

            <h2>⚖️ So sánh: 밖에 vs 만</h2>

            <table class="comparison-table">

                <thead>

                    <tr>

                        <th width="20%">Tiêu chí</th>

                        <th width="40%">밖에 (Ngoài ra không còn)</th>

                        <th width="40%">만 (Chỉ)</th>

                    </tr>

                </thead>

                <tbody>

                    <tr>

                        <td><strong>Đuôi câu</strong></td>

                        <td><span class="negative-highlight">Bắt buộc Phủ định</span><br>(안, 못, 없다, 모르다)</td>

                        <td>Khẳng định & Phủ định</td>

                    </tr>

                    <tr>

                        <td><strong>Sắc thái</strong></td>

                        <td>Tiêu cực, tiếc nuối, nhấn mạnh sự ít ỏi.</td>

                        <td>Trung tính, giới hạn phạm vi.</td>

                    </tr>

                    <tr>

                        <td><strong>Ví dụ</strong></td>

                        <td>물<span class="korean-highlight">밖에</span> 없어요.<br><em>(Chỉ còn mỗi nước thôi / Chả có gì ngoài nước).</em></td>

                        <td>물<span class="korean-highlight">만</span> 있어요.<br><em>(Chỉ có nước).</em></td>

                    </tr>

                </tbody>

            </table>

        </section>

  

    </div>

  

    <footer>

        Designed for The Free Korean Learners

    </footer>

  

</body>

</html>