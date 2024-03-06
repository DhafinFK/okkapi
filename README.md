# OKK-POSTMAN DOCUMENTATION

### Backend application ini adalah produk interpretasi saya terhadap [case study tugas Open Recruitment WebDev RISTEK 2024](https://docs.google.com/document/d/1gWl623f5ZCxWCdDkkuNm4ypcu9O4Udc6lycO1anOPM0/edit). Framework yang saya gunakan untuk membuat backend api ini aplikasi ini adalah Django-REST Framework. Serta menggunakan PostgreSQL sebagai DMBS aplikasi. Berikut adalah dokumentasi dan petunjuk menggunakan api yang telah dibuat.

## base url: http://localhost:8000/

## User Model

### URI Endpoint: api/auth/register/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `POST`        | username, email, password, npm | Username, Password | All User and non User |

<br>

### URI Endpoint: api/auth/login/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `POST`        | username, email, password, npm | Auth Token | All User and non User |

<br>

## Fakultas Model

### URI Endpoint: okkapi/fakultas/

| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nama, nama_panggilan | Superuser |
| `POST`        | nama, nama_panggilan | id, nama, nama_panggilan | Superuser |

### URI Endpoint: okkapi/fakultas/<fakultas_id>/

| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, nama_panggilan | Superuser |
| `DELETE`      |        -       |     ""    | Superuser |
| `PUT`         | nama, nama_panggilan | id, nama, nama_panggilan | Superuser |
| `PATCH`       | nama or nama_panggilan | id, nama, nama_panggilan | Superuser |

<br>

## Mahasiswa Model
### URI Endpoint: api/mahasiswa/


| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nama, npm, fakultas, angkatan | Superuser |
| `POST`        | id, nama, npm, fakultas_id, angkatan | id, nama, npm, fakultas, angkatan  | Superuser |


### URI Endpoint: api/mahasiswa/detail/<mahasiswa_id>/

| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, npm, fakultas, angkatan | Superuser |
| `DELETE`      |        -       |     ""    | Superuser |
| `PUT`         | nama, npm, fakultas_id, angkatan | id, nama, npm, fakultas, angkatan  | Superuser |
| `PATCH`       | nama, npm, fakultas_id, angkatan | id, nama, npm, fakultas, angkatan  | Superuser |

## Panitia Model

### URI Endpiont: api/mahasiswa/panitia/

| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, mahasiswa, jabatan, bidang | Superuser |
| `POST`        | jabatan, mahasiswa_id, bidang_id | id, mahasiswa, jabatan, bidang | Superuser |

### URI Endpoint: api/mahasiswa/panitia/<panitia_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, npm, fakultas, angkatan | Superuser |
| `DELETE`      |        -       |     ""    | Superuser |
| `PUT`         | jabatan, mahasiswa_id, bidang_id | id, mahasiswa, jabatan, bidang  | Superuser |
| `PATCH`       | jabatan, mahasiswa_id, bidang_id | id, mahasiswa, jabatan, bidang | Superuser |

## Mentor Model
### URI Endpoint: api/mahasiswa/mentor/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, mahasiswa, kelompok | Superuser |
| `POST`        | mahasiswa, nomor, mahasiswa_id | id, mahasiswa, kelompok | Superuser |


### URI Endpoint: api/mahasiswa/mentor/<mentor_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, mahasiswa, kelompok | Superuser |
| `DELETE`      |        -       |     ""    | Superuser |
| `PUT`         | mahasiswa, nomor, mahasiswa_id | id, mahasiswa, kelompok | Superuser |
| `PATCH`       | mahasiswa, nomor, mahasiswa_id | id, mahasiswa, kelompok | Superuser |

## Mentee Model
### URI Endpoint: api/mahasiswa/mentee/

| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, mahasiswa, kelompok, jalur_masuk | Superuser |
| `POST`        | nomor, mahasiswa_id, jalur_masuk | id, mahasiswa, kelompok, jalur_masuk | Superuser |

### URI Endpoint: api/mahasiswa/mentee/<mentee_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, mahasiswa, kelompok, jalur_masuk | Superuser |
| `DELETE`      |        -       |     ""    | Superuser |
| `PUT`         | nomor, mahasiswa_id, jalur_masuk | id, mahasiswa, kelompok, jalur_masuk | Superuser |
| `PATCH`       | nomor, mahasiswa_id, jalur_masuk | id, mahasiswa, kelompok, jalur_masuk| Superuser |

## BidangPanitia Model

### URI Endpoint: api/bidang/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nama, bidang_panitia, anggota | Superuser, Panitia |
| `POST`        | nama, bidang_panitia | id, nama, bidang_panitia, anggota | Superuser, Panitia |

### URI Endpoint: api/bidang/<bidang_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, bidang_panitia, anggota | Superuser, Panitia |
| `DELETE`      |        -       |     ""    | Superuser, Panitia |
| `PUT`         | nama, bidang_panitia | id, nama, bidang_panitia, anggota | Superuser, Panitia |
| `PATCH`       | nama, bidang_panitia | id, nama, bidang_panitia, anggota | Superuser, Panitia |

## Rapat Model

### URI Endpoint: api/bidang/<bidang_id>/sessions/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, bidang, date, start_time, end_time, attendees | Superuser, Panitia |
| `POST`        | bidang, date, start_time, end_time, attendees | id, bidang, date, start_time, end_time, attendees | Superuser, Panitia |

### URI Endpoint: api/bidang/<bidang_id>/sessions/<session_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       |id, bidang, date, start_time, end_time, attendees | Superuser, Panitia |
| `DELETE`      |        -       |     ""    | Superuser, Panitia |
| `PUT`         | bidang, date, start_time, end_time, attendees | id, bidang, date, start_time, end_time, attendees | Superuser, Panitia |
| `PATCH`       | bidang, date, start_time, end_time, attendees | id, bidang, date, start_time, end_time, attendees | Superuser, Panitia |

## Kelompok Model

### URI Endpoint: api/kelompok/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nomor, mentor | Superuser, Mentor |
| `POST`        | nomor | id, nomor, mentor | Superuser, Mentor |

### URI Endpoint: api/kelompok/<kelompok_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nomor, mentor | Superuser, Mentor  |
| `DELETE`      |        -       |     ""    | Superuser, Mentor  |
| `PUT`         | nomor | id, nomor, mentor | Superuser, Mentor  |
| `PATCH`       | nomor | id, nomor, mentor| Superuser, Mentor  |

## Mentoring Model

### URI Endpoint: api/kelompok/<kelompok_id>/sessions/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, kelompok, date, start_time, end_time, attendees | Superuser, Mentor |
| `POST`        | kelompok, date, start_time, end_time, attendees | id, kelompok, date, start_time, end_time, attendees | Superuser, Mentor |

### URI Enpoint: api/kelompok/<kelompok_id>/sessions/<sessions_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, kelompok, date, start_time, end_time, attendees | Superuser, Mentor  |
| `DELETE`      |        -       |     ""    | Superuser, Mentor  |
| `PUT`         | kelompok, date, start_time, end_time, attendees | id, kelompok, date, start_time, end_time, attendees | Superuser, Mentor  |
| `PATCH`       | kelompok, date, start_time, end_time, attendees | id, kelompok, date, start_time, end_time, attendees| Superuser, Mentor  |

## Acara Model
### URI Endpoint: api/acara/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nama, waktu_mulai, waktu_selesai, pembicara_list, paket_sponsorship | Superuser, Panitia |
| `POST`        | nama, waktu_mulai, waktu_selesai, pembicara_list | id, nama, waktu_mulai, waktu_selesai, pembicara_list, paket_sponsorship | Superuser, Panitia |

### URI Endpoint: api/acara/detail/<acara_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, waktu_mulai, waktu_selesai, pembicara_list, paket_sponsorship | Superuser, Panitia  |
| `DELETE`      |        -       |     ""    | Superuser, Panitia |
| `PUT`         | nama, waktu_mulai, waktu_selesai, pembicara_list | id, nama, waktu_mulai, waktu_selesai, pembicara_list, paket_sponsorship | Superuser, Panitia |
| `PATCH`       | nama, waktu_mulai, waktu_selesai, pembicara_list | id, nama, waktu_mulai, waktu_selesai, pembicara_list, paket_sponsorship | Superuser, Panitia |

## Acara Pembicara
### URI Endpiont: api/acara/pembicara/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nama, mengisi_acara | Superuser, Panitia |
| `POST`        | nama | id, nama, mengisi_acara | Superuser, Panitia |

### URI Endpoint: api/acara/pembicara/<pembicara_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, mengisi_acara | Superuser, Panitia  |
| `DELETE`      |        -       |     ""    | Superuser, Panitia |
| `PUT`         | nama | id, nama, mengisi_acara | Superuser, Panitia |
| `PATCH`       | nama | id, nama, mengisi_acara | Superuser, Panitia |

## Sponsor Model
### URI Endpoint: api/acara/sponsor/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, nama, paket_sponsor | Superuser, Panitia |
| `POST`        | nama | id, nama, paket_sponsor | Superuser, Panitia |

### URI Endpoint: api/acara/sponsor/<sponsor_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, paket_sponsor | Superuser, Panitia  |
| `DELETE`      |        -       |     ""    | Superuser, Panitia |
| `PUT`         | nama | id, nama, paket_sponsor | Superuser, Panitia |
| `PATCH`       | nama | id, nama, paket_sponsor | Superuser, Panitia |

## SponsorAcara Model
### URI Endpoint: api/acara/sponsor-acara/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |       -        | id, sponsor_id, acara_id, package | Superuser, Panitia |
| `POST`        | sponsor_id, acara_id, package | id, sponsor_id, acara_id, package | Superuser, Panitia |


### URI Endpoint: api/acara/sponsor-acara/<sponsor_acara_id>/
| METHOD        | JSON-ARGUMENTS | RETURNS   | AUTHORIZED USERS |
| :-----------: | :------------: | :-------: | :--------------: |
| `GET`         |        -       | id, nama, paket_sponsor | Superuser, Panitia  |
| `DELETE`      |        -       |     ""    | Superuser, Panitia |
| `PUT`         | sponsor_id, acara_id, package | id, sponsor_id, acara_id, package | Superuser, Panitia |
| `PATCH`       | sponsor_id, acara_id, package | id, sponsor_id, acara_id, package | Superuser, Panitia |