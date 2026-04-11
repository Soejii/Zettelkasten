/**
 * Auto-generates the research Google Form.
 * Block randomization: items randomized within each scale section.
 * Participants are blinded — no instrument names shown.
 * Scoring key: see "Kunci Skoring - Randomisasi Item.md"
 *
 * HOW TO USE:
 * 1. Go to script.google.com
 * 2. Create a new project
 * 3. Paste this entire file
 * 4. Click Run → createResearchForm
 * 5. Authorize when prompted
 * 6. Check Execution Log for your form URLs
 */

function createResearchForm() {

  // ============================================================
  // ITEM DATA
  // Block A: GMS (4-point), randomized within block
  // Block B: ARS-30 (6-point), randomized within block
  // ============================================================

  var scale4 = [
    '1 - Sangat Tidak Setuju',
    '2 - Tidak Setuju',
    '3 - Setuju',
    '4 - Sangat Setuju'
  ];

  var scale6 = [
    '1 - Sangat Tidak Setuju',
    '2 - Tidak Setuju',
    '3 - Agak Tidak Setuju',
    '4 - Agak Setuju',
    '5 - Setuju',
    '6 - Sangat Setuju'
  ];

  // Block A — GMS items (randomized order, 4-point scale)
  // Original code → form position mapping in scoring key
  var gmsItems = [
    'Sejujurnya, saya berpikir tidak bisa mengubah kecerdasan saya.',                                                                     // GMS-3 (R)
    'Terlepas dari tingkat kecerdasan saya saat ini, saya berpikir punya kapasitas untuk mengubahnya walau sedikit.',                     // GMS-7 (F)
    'Saya merasa tidak bisa berbuat banyak untuk meningkatkan kecerdasan saya.',                                                          // GMS-1 (R)
    'Dengan waktu dan usaha yang cukup, saya pikir saya bisa meningkatkan kecerdasan saya secara signifikan.',                            // GMS-5 (F)
    'Saya mampu mempelajari hal-hal baru, tapi saya tidak mampu mengubah tingkat kecerdasan saya.',                                       // GMS-4 (R)
    'Saya percaya, saya memiliki kemampuan untuk mengubah kecerdasan saya cukup banyak seiring waktu.',                                   // GMS-8 (F)
    'Kecerdasan saya adalah sesuatu tentang diri saya yang tidak banyak bisa diubah.',                                                    // GMS-2 (R)
    'Saya percaya, saya selalu bisa meningkatkan kecerdasan saya secara signifikan.',                                                     // GMS-6 (F)
  ];

  // Block B — ARS-30 items (randomized order, 6-point scale)
  var arsItems = [
    'Saya akan tetap berusaha.',                                                                                                           // ARS-16 (F)
    'Saya akan mulai berpikir kesempatan saya untuk sukses di universitas adalah kecil.',                                                  // ARS-7  (R)
    'Saya akan mencoba berbagai cara yang berbeda untuk belajar.',                                                                         // ARS-24 (F)
    'Saya akan menyerah saja.',                                                                                                            // ARS-3  (R)
    'Saya akan mulai memantau dan mengevaluasi pencapaian dan upaya saya.',                                                                // ARS-20 (F)
    'Saya akan belajar lebih keras.',                                                                                                      // ARS-11 (F)
    'Saya akan merasa semuanya hancur dan salah.',                                                                                         // ARS-28 (R)
    'Saya akan menggunakan situasi ini untuk memotivasi diri saya sendiri.',                                                               // ARS-4  (F)
    'Saya akan mencoba memikirkan solusi baru.',                                                                                           // ARS-13 (F)
    'Saya mungkin akan merasa terganggu.',                                                                                                 // ARS-6  (R)
    'Saya akan menetapkan tujuan yang ingin saya capai.',                                                                                  // ARS-25 (F)
    'Saya tidak akan menerima umpan balik dari dosen.',                                                                                    // ARS-1  (R)
    'Saya tidak akan mengubah tujuan dan ambisi jangka panjang saya.',                                                                     // ARS-17 (F)
    'Saya akan mulai berpikir bahwa kesempatan saya untuk mendapat pekerjaan kecil.',                                                      // ARS-19 (R)
    'Saya akan melihat situasi ini sebagai tantangan.',                                                                                    // ARS-8  (F)
    'Saya akan mencoba untuk lebih memahami kekuatan dan kelemahan saya untuk membantu saya bekerja lebih baik.',                         // ARS-27 (F)
    'Saya mungkin akan mengalami depresi.',                                                                                                // ARS-12 (R)
    'Saya berharap dapat menunjukkan bahwa saya dapat meningkatkan nilai saya.',                                                           // ARS-30 (F)
    'Saya akan menggunakan umpan balik untuk meningkatkan kualitas tugas/pekerjaan saya.',                                                 // ARS-2  (F)
    'Saya akan menyalahkan dosen.',                                                                                                        // ARS-15 (R)
    'Saya akan berusaha semaksimal mungkin untuk berhenti memikirkan hal-hal negatif.',                                                    // ARS-9  (F)
    'Saya akan memberikan dukungan untuk diri saya sendiri.',                                                                              // ARS-22 (F)
    'Saya akan merasa sangat kecewa.',                                                                                                     // ARS-14 (R)
    'Saya akan mencari dukungan dari keluarga dan teman-teman saya.',                                                                      // ARS-26 (F)
    'Saya akan mengubah rencana karir saya.',                                                                                              // ARS-5  (F)
    'Saya akan menggunakan kesuksesan saya sebelumnya untuk membantu memotivasi diri saya.',                                               // ARS-18 (F)
    'Saya akan melihat situasi ini sebagai kondisi sementara.',                                                                            // ARS-10 (F)
    'Saya akan mulai memberlakukan hadiah dan hukuman pada diri saya bergantung pada kinerja saya.',                                       // ARS-29 (F)
    'Saya akan mencari bantuan dari dosen saya.',                                                                                          // ARS-21 (F)
    'Saya akan berusaha untuk tidak panik.',                                                                                               // ARS-23 (F)
  ];

  // ============================================================
  // CREATE FORM
  // ============================================================
  var form = FormApp.create('Survei Pengalaman Akademik Mahasiswa Indonesia');
  form.setDescription('Penelitian ini bertujuan untuk memahami pengalaman dan keyakinan mahasiswa dalam menghadapi kehidupan akademik.');
  form.setIsQuiz(false);
  form.setAllowResponseEdits(false);
  form.setLimitOneResponsePerUser(false);

  // ============================================================
  // BAGIAN 1 — INFORMED CONSENT
  // ============================================================
  form.addSectionHeaderItem()
    .setTitle('LEMBAR INFORMASI DAN PERSETUJUAN PARTISIPAN')
    .setHelpText(
      'Yth. Calon Partisipan,\n\n' +
      'Saya Rafi Mahadika Sujianto, mahasiswa Program Studi Psikologi, mengundang Anda untuk berpartisipasi dalam penelitian berjudul "Survei Pengalaman Akademik Mahasiswa Indonesia". ' +
      'Penelitian ini dilakukan sebagai bagian dari tugas mata kuliah Penelitian Psikologi Kuantitatif.\n\n' +
      '─────────────────────────────\n' +
      'TUJUAN PENELITIAN\n' +
      'Memahami keyakinan dan pengalaman mahasiswa dalam menghadapi tantangan akademik.\n\n' +
      'PROSEDUR\n' +
      'Anda akan diminta mengisi kuesioner daring. Pengisian membutuhkan waktu sekitar 10–15 menit.\n\n' +
      'KERAHASIAAN DATA\n' +
      'Seluruh data yang Anda berikan bersifat rahasia dan hanya digunakan untuk keperluan penelitian ini. Identitas Anda tidak akan dipublikasikan dalam bentuk apapun.\n\n' +
      'KESUKARELAAN\n' +
      'Partisipasi Anda bersifat sukarela. Anda berhak untuk menghentikan pengisian kapan saja tanpa konsekuensi apapun.\n\n' +
      'PERTANYAAN\n' +
      'Jika Anda memiliki pertanyaan, silakan hubungi peneliti melalui email: [email peneliti]\n' +
      '─────────────────────────────'
    );

  form.addCheckboxItem()
    .setTitle('Pernyataan Persetujuan')
    .setHelpText(
      'Dengan mencentang pilihan di bawah, Anda menyatakan bahwa:\n' +
      '• Anda telah membaca dan memahami informasi di atas\n' +
      '• Anda berusia 18 tahun atau lebih\n' +
      '• Anda merupakan mahasiswa aktif di perguruan tinggi Indonesia\n' +
      '• Anda bersedia berpartisipasi secara sukarela'
    )
    .setChoiceValues(['Saya menyetujui dan bersedia berpartisipasi dalam penelitian ini'])
    .setRequired(true);

  // ============================================================
  // BAGIAN 2 — DATA DEMOGRAFIS
  // ============================================================
  form.addPageBreakItem()
    .setTitle('BAGIAN 2 — DATA DEMOGRAFIS');

  form.addTextItem()
    .setTitle('Nama (inisial)')
    .setRequired(true);

  form.addTextItem()
    .setTitle('Usia')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Jenis kelamin')
    .setChoiceValues(['Laki-laki', 'Perempuan'])
    .setRequired(true);

  form.addTextItem()
    .setTitle('Program studi')
    .setRequired(true);

  form.addTextItem()
    .setTitle('Perguruan tinggi')
    .setRequired(true);

  form.addTextItem()
    .setTitle('Semester saat ini')
    .setRequired(true);

  // ============================================================
  // BAGIAN 3 — PERNYATAAN BAGIAN A (GMS, 4-point, blinded)
  // ============================================================
  form.addPageBreakItem()
    .setTitle('BAGIAN 3 — PERNYATAAN A')
    .setHelpText(
      'Petunjuk: Bacalah setiap pernyataan berikut dengan seksama. ' +
      'Pilih angka yang paling menggambarkan tingkat kesetujuan Anda.\n\n' +
      '1 = Sangat Tidak Setuju\n' +
      '2 = Tidak Setuju\n' +
      '3 = Setuju\n' +
      '4 = Sangat Setuju\n\n' +
      'Tidak ada jawaban yang benar atau salah.'
    );

  for (var i = 0; i < gmsItems.length; i++) {
    form.addMultipleChoiceItem()
      .setTitle((i + 1) + '. ' + gmsItems[i])
      .setChoiceValues(scale4)
      .setRequired(true);
  }

  // ============================================================
  // BAGIAN 4 — PERNYATAAN BAGIAN B (ARS-30, 6-point, blinded)
  // ============================================================
  form.addPageBreakItem()
    .setTitle('BAGIAN 4 — PERNYATAAN B')
    .setHelpText(
      'Petunjuk: Bayangkan Anda sedang menghadapi situasi yang sulit atau mengecewakan dalam perkuliahan. ' +
      'Bacalah setiap pernyataan berikut dan pilih angka yang paling menggambarkan apa yang kemungkinan besar akan Anda lakukan atau rasakan.\n\n' +
      '1 = Sangat Tidak Setuju\n' +
      '2 = Tidak Setuju\n' +
      '3 = Agak Tidak Setuju\n' +
      '4 = Agak Setuju\n' +
      '5 = Setuju\n' +
      '6 = Sangat Setuju\n\n' +
      'Tidak ada jawaban yang benar atau salah.'
    );

  for (var j = 0; j < arsItems.length; j++) {
    form.addMultipleChoiceItem()
      .setTitle((j + 1) + '. ' + arsItems[j])
      .setChoiceValues(scale6)
      .setRequired(true);
  }

  // ============================================================
  // DONE — LOG URLS
  // ============================================================
  Logger.log('========================================');
  Logger.log('FORM BERHASIL DIBUAT!');
  Logger.log('Link untuk responden : ' + form.getPublishedUrl());
  Logger.log('Link untuk edit form : ' + form.getEditUrl());
  Logger.log('========================================');
}
