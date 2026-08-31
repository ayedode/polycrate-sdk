from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_scm_repositories_archive_create_annotations_error_component import (
        ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_archived_at_error_component import (
        ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_archived_error_component import (
        ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_archived_reason_error_component import (
        ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_credential_error_component import (
        ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_criticality_error_component import (
        ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_debug_mode_error_component import (
        ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_display_name_error_component import (
        ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_groups_count_error_component import (
        ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_hostname_error_component import (
        ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_k8s_app_error_component import (
        ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_k8s_cluster_error_component import (
        ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_kind_error_component import (
        ApiV1ScmRepositoriesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_labels_error_component import (
        ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_metadata_error_component import (
        ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_name_error_component import (
        ApiV1ScmRepositoriesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_non_field_errors_error_component import (
        ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_platform_service_error_component import (
        ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_projects_count_error_component import (
        ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_provider_error_component import (
        ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_provider_id_error_component import (
        ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_provider_reference_error_component import (
        ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_reconciliation_enabled_error_component import (
        ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_repository_version_error_component import (
        ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_sla_availability_error_component import (
        ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_sla_target_error_component import (
        ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_slo_availability_error_component import (
        ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_slo_target_error_component import (
        ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_target_availability_error_component import (
        ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_tolerations_error_component import (
        ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_archive_create_users_count_error_component import (
        ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ScmRepositoriesArchiveCreateValidationError")


@_attrs_define
class ApiV1ScmRepositoriesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent | ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent
            | ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateKindErrorComponent | ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponent | ApiV1ScmRepositoriesArchiveCreateNameErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent |
            ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateKindErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateNameErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent
        | ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_scm_repositories_archive_create_annotations_error_component import (
            ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_archived_at_error_component import (
            ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_archived_error_component import (
            ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_archived_reason_error_component import (
            ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_credential_error_component import (
            ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_criticality_error_component import (
            ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_debug_mode_error_component import (
            ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_display_name_error_component import (
            ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_groups_count_error_component import (
            ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_hostname_error_component import (
            ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_k8s_app_error_component import (
            ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_kind_error_component import (
            ApiV1ScmRepositoriesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_labels_error_component import (
            ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_name_error_component import (
            ApiV1ScmRepositoriesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_non_field_errors_error_component import (
            ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_platform_service_error_component import (
            ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_projects_count_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_provider_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_provider_id_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_provider_reference_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_repository_version_error_component import (
            ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_sla_availability_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_sla_target_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_slo_availability_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_slo_target_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_target_availability_error_component import (
            ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_tolerations_error_component import (
            ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_users_count_error_component import (
            ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent):
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
        from ..models.api_v1_scm_repositories_archive_create_annotations_error_component import (
            ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_archived_at_error_component import (
            ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_archived_error_component import (
            ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_archived_reason_error_component import (
            ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_credential_error_component import (
            ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_criticality_error_component import (
            ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_debug_mode_error_component import (
            ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_display_name_error_component import (
            ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_groups_count_error_component import (
            ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_hostname_error_component import (
            ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_k8s_app_error_component import (
            ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_kind_error_component import (
            ApiV1ScmRepositoriesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_labels_error_component import (
            ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_metadata_error_component import (
            ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_name_error_component import (
            ApiV1ScmRepositoriesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_non_field_errors_error_component import (
            ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_platform_service_error_component import (
            ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_projects_count_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_provider_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_provider_id_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_provider_reference_error_component import (
            ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_repository_version_error_component import (
            ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_sla_availability_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_sla_target_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_slo_availability_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_slo_target_error_component import (
            ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_target_availability_error_component import (
            ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_tolerations_error_component import (
            ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_archive_create_users_count_error_component import (
            ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateKindErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateNameErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent
                | ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_0 = (
                        ApiV1ScmRepositoriesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_1 = (
                        ApiV1ScmRepositoriesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_2 = (
                        ApiV1ScmRepositoriesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_3 = (
                        ApiV1ScmRepositoriesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_4 = (
                        ApiV1ScmRepositoriesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_5 = (
                        ApiV1ScmRepositoriesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_6 = (
                        ApiV1ScmRepositoriesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_7 = (
                        ApiV1ScmRepositoriesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_8 = (
                        ApiV1ScmRepositoriesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_9 = (
                        ApiV1ScmRepositoriesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_10 = (
                        ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_11 = (
                        ApiV1ScmRepositoriesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_12 = (
                        ApiV1ScmRepositoriesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_13 = (
                        ApiV1ScmRepositoriesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_14 = (
                        ApiV1ScmRepositoriesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_15 = (
                        ApiV1ScmRepositoriesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_16 = (
                        ApiV1ScmRepositoriesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_17 = (
                        ApiV1ScmRepositoriesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_18 = (
                        ApiV1ScmRepositoriesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_19 = (
                        ApiV1ScmRepositoriesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_20 = (
                        ApiV1ScmRepositoriesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_21 = (
                        ApiV1ScmRepositoriesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_22 = (
                        ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_23 = (
                        ApiV1ScmRepositoriesArchiveCreateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_24 = (
                        ApiV1ScmRepositoriesArchiveCreateUsersCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_25 = (
                        ApiV1ScmRepositoriesArchiveCreateGroupsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_26 = (
                        ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_27 = (
                        ApiV1ScmRepositoriesArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_28 = (
                        ApiV1ScmRepositoriesArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_archive_create_error_type_29 = (
                        ApiV1ScmRepositoriesArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_scm_repositories_archive_create_error_type_30 = (
                    ApiV1ScmRepositoriesArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_scm_repositories_archive_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_scm_repositories_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_scm_repositories_archive_create_validation_error.additional_properties = d
        return api_v1_scm_repositories_archive_create_validation_error

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
