from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_registry_registries_archive_create_annotations_error_component import (
        ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_archived_at_error_component import (
        ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_archived_error_component import (
        ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_archived_reason_error_component import (
        ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_credential_error_component import (
        ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_criticality_error_component import (
        ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_debug_mode_error_component import (
        ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_display_name_error_component import (
        ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_hostname_error_component import (
        ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_k8s_app_error_component import (
        ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_k8s_cluster_error_component import (
        ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_kind_error_component import (
        ApiV1RegistryRegistriesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_labels_error_component import (
        ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_metadata_error_component import (
        ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_name_error_component import (
        ApiV1RegistryRegistriesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_non_field_errors_error_component import (
        ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_platform_service_error_component import (
        ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_projects_count_error_component import (
        ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_provider_error_component import (
        ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_provider_id_error_component import (
        ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_provider_reference_error_component import (
        ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_reconciliation_enabled_error_component import (
        ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_registry_version_error_component import (
        ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_repositories_count_error_component import (
        ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_sla_availability_error_component import (
        ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_sla_target_error_component import (
        ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_slo_availability_error_component import (
        ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_slo_target_error_component import (
        ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_storage_used_bytes_error_component import (
        ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_target_availability_error_component import (
        ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_archive_create_tolerations_error_component import (
        ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegistryRegistriesArchiveCreateValidationError")


@_attrs_define
class ApiV1RegistryRegistriesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateKindErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateNameErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateKindErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateNameErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_registry_registries_archive_create_annotations_error_component import (
            ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_archived_at_error_component import (
            ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_archived_error_component import (
            ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_archived_reason_error_component import (
            ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_credential_error_component import (
            ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_criticality_error_component import (
            ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_debug_mode_error_component import (
            ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_display_name_error_component import (
            ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_hostname_error_component import (
            ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_k8s_app_error_component import (
            ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_kind_error_component import (
            ApiV1RegistryRegistriesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_labels_error_component import (
            ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_name_error_component import (
            ApiV1RegistryRegistriesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_non_field_errors_error_component import (
            ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_platform_service_error_component import (
            ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_projects_count_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_provider_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_provider_id_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_provider_reference_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_registry_version_error_component import (
            ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_repositories_count_error_component import (
            ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_sla_availability_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_sla_target_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_slo_availability_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_slo_target_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_target_availability_error_component import (
            ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_tolerations_error_component import (
            ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_registry_registries_archive_create_annotations_error_component import (
            ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_archived_at_error_component import (
            ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_archived_error_component import (
            ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_archived_reason_error_component import (
            ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_credential_error_component import (
            ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_criticality_error_component import (
            ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_debug_mode_error_component import (
            ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_display_name_error_component import (
            ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_hostname_error_component import (
            ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_k8s_app_error_component import (
            ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_kind_error_component import (
            ApiV1RegistryRegistriesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_labels_error_component import (
            ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_metadata_error_component import (
            ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_name_error_component import (
            ApiV1RegistryRegistriesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_non_field_errors_error_component import (
            ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_platform_service_error_component import (
            ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_projects_count_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_provider_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_provider_id_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_provider_reference_error_component import (
            ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_registry_version_error_component import (
            ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_repositories_count_error_component import (
            ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_sla_availability_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_sla_target_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_slo_availability_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_slo_target_error_component import (
            ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_target_availability_error_component import (
            ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_archive_create_tolerations_error_component import (
            ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateKindErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateNameErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_0 = (
                        ApiV1RegistryRegistriesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_1 = (
                        ApiV1RegistryRegistriesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_2 = (
                        ApiV1RegistryRegistriesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_3 = (
                        ApiV1RegistryRegistriesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_4 = (
                        ApiV1RegistryRegistriesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_5 = (
                        ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_6 = (
                        ApiV1RegistryRegistriesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_7 = (
                        ApiV1RegistryRegistriesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_8 = (
                        ApiV1RegistryRegistriesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_9 = (
                        ApiV1RegistryRegistriesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_10 = (
                        ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_11 = (
                        ApiV1RegistryRegistriesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_12 = (
                        ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_13 = (
                        ApiV1RegistryRegistriesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_14 = (
                        ApiV1RegistryRegistriesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_15 = (
                        ApiV1RegistryRegistriesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_16 = (
                        ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_17 = (
                        ApiV1RegistryRegistriesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_18 = (
                        ApiV1RegistryRegistriesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_19 = (
                        ApiV1RegistryRegistriesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_20 = (
                        ApiV1RegistryRegistriesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_21 = (
                        ApiV1RegistryRegistriesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_22 = (
                        ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_23 = (
                        ApiV1RegistryRegistriesArchiveCreateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_24 = (
                        ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_25 = (
                        ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_26 = (
                        ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_27 = (
                        ApiV1RegistryRegistriesArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_28 = (
                        ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_archive_create_error_type_29 = (
                        ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_registry_registries_archive_create_error_type_30 = (
                    ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_registry_registries_archive_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_registry_registries_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_registry_registries_archive_create_validation_error.additional_properties = d
        return api_v1_registry_registries_archive_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
