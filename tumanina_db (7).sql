-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Des 2024 pada 01.42
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tumanina_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `articles`
--

INSERT INTO `articles` (`id`, `title`, `content`, `image`) VALUES
(10, 'bangsl', 'bbboos\n', 'WhatsApp_Image_2024-11-30_at_00.03.38_5248b2b2.jpg'),
(13, 'bangtoni', 'banggsgsg\n', 'Login__Register_ScreenUI_UX_Design.jpeg'),
(18, 'sholat dhuha', 'melancarkan rezeki\n', NULL),
(19, 'sholat dhuha', 'melancarkan rezeki\n', NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `hasil_model`
--

CREATE TABLE `hasil_model` (
  `id_hasil_model` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `tanggal` date NOT NULL,
  `review` varchar(255) NOT NULL,
  `label` varchar(255) NOT NULL,
  `id_review` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `hasil_model`
--

INSERT INTO `hasil_model` (`id_hasil_model`, `nama`, `tanggal`, `review`, `label`, `id_review`) VALUES
(23, 'hai', '2024-12-23', 'aplikasinya keren banget', 'Positif', 22);

-- --------------------------------------------------------

--
-- Struktur dari tabel `input_review`
--

CREATE TABLE `input_review` (
  `id_review` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `tanggal` date NOT NULL,
  `review` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `input_review`
--

INSERT INTO `input_review` (`id_review`, `nama`, `tanggal`, `review`) VALUES
(22, 'hai', '2024-12-23', 'aplikasinya keren banget');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('super_admin','admin') NOT NULL DEFAULT 'admin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(28, 'adminsuper', 'scrypt:32768:8:1$jcBNlL5bhebX5jMk$50563d9370fc28442928de350c5b9c95935351124c816e219ec94a61d95e8a17a70f124754c33d441dde958571c13fb5357aae97c8c27cb8acf6d29720f4ea31', 'super_admin'),
(35, 'adminbiasa', 'scrypt:32768:8:1$q20Nd3Qy6dK2NHyH$2a0dc7df44118a85d6c211c508f29d9fe764bf24be1d6772f422ab78a26914783ac9ee07008d9fc194e0db52112b8c5f566c1449bb13e51ed9ac39f2b59fe1bb', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `hasil_model`
--
ALTER TABLE `hasil_model`
  ADD PRIMARY KEY (`id_hasil_model`);

--
-- Indeks untuk tabel `input_review`
--
ALTER TABLE `input_review`
  ADD PRIMARY KEY (`id_review`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT untuk tabel `hasil_model`
--
ALTER TABLE `hasil_model`
  MODIFY `id_hasil_model` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `input_review`
--
ALTER TABLE `input_review`
  MODIFY `id_review` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
