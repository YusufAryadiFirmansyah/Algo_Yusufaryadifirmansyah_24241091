import java.util.Scanner;

public class GajiPegawai {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input data pegawai
        System.out.print("Masukkan nama pegawai: ");
        String namaPegawai = scanner.nextLine();

        System.out.print("Masukkan status pegawai (tetap/tidak tetap): ");
        String statusPegawai = scanner.nextLine().toLowerCase();

        System.out.print("Masukkan gaji pokok: Rp. ");
        double gajiPokok = scanner.nextDouble();

        System.out.print("Masukkan durasi lembur (jam): ");
        double durasiLembur = scanner.nextDouble();

        // Perhitungan
        double tunjangan;
        double lembur;
        double gajiBersih;

        if (statusPegawai.equals("tetap")) {
            // Pegawai tetap
            tunjangan = 0.1 * gajiPokok;
            lembur = durasiLembur * (0.1 * gajiPokok);
            gajiBersih = gajiPokok + tunjangan + lembur;
        } else {
            // Pegawai tidak tetap
            tunjangan = 0;
            lembur = durasiLembur * (0.05 * gajiPokok);
            gajiBersih = gajiPokok + lembur;
        }

        // Output
        System.out.println("\n--- Rincian Gaji Pegawai ---");
        System.out.printf("Nama Pegawai : %s%n", namaPegawai);
        System.out.printf("Gaji Pokok : Rp%,.2f%n", gajiPokok);
        System.out.printf("Tunjangan : Rp%,.2f%n", tunjangan);
        System.out.printf("Durasi Lembur : %.0f jam%n", durasiLembur);
        System.out.printf("Gaji Bersih : Rp%,.2f%n", gajiBersih);

        scanner.close();
    }
}