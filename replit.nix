{ pkgs }: {
  deps = [
    pkgs.sqlite-interactive.bin
    pkgs.imagemagick
    pkgs.import queries
    pkgs.sqlite.bin
  ];
}