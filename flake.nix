{
	description = "voice_channel_notifier";

	inputs.nixpkgs.url = "github:NixOS/nixpkgs";

	outputs = { self, nixpkgs }:

	let
		system = "aarch64-darwin";
		pkgs = import nixpkgs { inherit system; };
	in {
		devShells = { "${system}" = { default = pkgs.mkShell { buildInputs = [
			pkgs.python313
			pkgs.python313Packages.pip
			pkgs.git
		];};};};
	};
}
