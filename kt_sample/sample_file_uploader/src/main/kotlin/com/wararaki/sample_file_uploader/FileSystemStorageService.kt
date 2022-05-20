package com.wararaki.sample_file_uploader

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.core.io.Resource
import org.springframework.core.io.UrlResource
import org.springframework.stereotype.Service
import org.springframework.util.FileSystemUtils
import org.springframework.web.multipart.MultipartFile
import java.io.IOException
import java.io.InputStream
import java.net.MalformedURLException
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths
import java.nio.file.StandardCopyOption
import java.util.stream.Stream

@Service
class FileSystemStorageService: StorageService {
    private var rootLocation: Path

    @Autowired
    constructor(storageProperties: StorageProperties) {
        this.rootLocation = Paths.get(storageProperties.getLocation())
    }

    override fun store(file: MultipartFile) {
        try {
            if (file.isEmpty) {
                throw StorageException("Failed to store empty file")
            }
            val destinationFile = this.rootLocation.resolve(
                Paths.get(file.originalFilename)
            ).normalize().toAbsolutePath()

            if (!destinationFile.parent.equals(this.rootLocation.toAbsolutePath())) {
                throw StorageException("Cannot store file outside current directory")
            }

            try {
                file.inputStream.use { ist -> Files.copy(ist, destinationFile, StandardCopyOption.REPLACE_EXISTING) }
            }
            catch (e: Exception) {
                e.printStackTrace()
            }
        }
        catch (e: IOException) {
            throw StorageException("Failed to store file.", e)
        }
    }

    override fun loadAll(): Stream<Path> {
        try {
            return Files.walk(this.rootLocation, 1).filter {path -> !path.equals(this.rootLocation)}.map(this.rootLocation::relativize)
        }
        catch (e: IOException) {
            throw StorageException("Failed to read stored files", e)
        }
    }

    override fun load(filename: String): Path {
        return rootLocation.resolve(filename)
    }

    override fun loadAsResource(filename: String): Resource {
        try {
            val file = load(filename)
            val resource = UrlResource(file.toUri())

            if (resource.exists() || resource.isReadable) {
                return resource
            }
            else {
                throw StorageFileNotFoundException("Could not read file: %s".format(filename))
            }
        }
        catch (e: MalformedURLException) {
            throw StorageFileNotFoundException("Could not read file: %s".format(filename), e)
        }
    }

    override fun deleteAll() {
        FileSystemUtils.deleteRecursively(rootLocation.toFile())
    }

    override fun init() {
        try {
            Files.createDirectories(rootLocation)
        }
        catch (e: IOException) {
            throw StorageException("Could not initialize storage", e)
        }
    }
}