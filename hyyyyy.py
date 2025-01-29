<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leela Banoo</title>
    <style>
        /* Background Gradient */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            background: linear-gradient(to right, #ff7f50, #ff6347, #ff4500);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: white;
            overflow: hidden;
        }
        
        h1 {
            font-size: 4rem;
            color: white;
            opacity: 0;
            transform: translateY(50px);
            animation: fadeInUp 3s ease-out forwards;
            font-family: 'Brush Script MT', cursive; /* Stylish font */
        }

        /* Animation */
        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(50px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Floating Flowers */
        .flower {
            position: absolute;
            width: 50px;
            height: 50px;
            background-size: cover;
            animation: floatAnimation linear infinite;
        }

        .flower1 { background-image: url('https://upload.wikimedia.org/wikipedia/commons/5/56/Red_rose.png'); }
        .flower2 { background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/3e/Blue_floral_silhouette.jpg'); }
        .flower3 { background-image: url('https://upload.wikimedia.org/wikipedia/commons/6/6d/Flower_svg.svg'); }

        /* Floating animation */
        @keyframes floatAnimation {
            0% {
                transform: translateY(0px) translateX(0px) rotate(0deg);
                opacity: 1;
            }
            50% {
                transform: translateY(-50px) translateX(20px) rotate(20deg);
                opacity: 0.8;
            }
            100% {
                transform: translateY(0px) translateX(0px) rotate(0deg);
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <h1>Leela Banoo</h1>

    <script>
        // Function to create animated flowers dynamically
        function createFlower() {
            const flower = document.createElement("div");
            flower.classList.add("flower");

            // Randomly select a flower type
            const flowerTypes = ["flower1", "flower2", "flower3"];
            flower.classList.add(flowerTypes[Math.floor(Math.random() * flowerTypes.length)]);

            // Set random position
            flower.style.left = Math.random() * window.innerWidth + "px";
            flower.style.top = Math.random() * window.innerHeight + "px";

            // Set random animation duration & delay
            flower.style.animationDuration = (Math.random() * 5 + 5) + "s";
            flower.style.animationDelay = Math.random() * 2 + "s";

            document.body.appendChild(flower);

            // Remove flower after animation
            setTimeout(() => {
                flower.remove();
            }, 10000);
        }

        // Generate flowers at random intervals
        setInterval(createFlower, 1000);
    </script>
</body>
</html>
