from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_scm_repositories_create_annotations_error_component import (
        ApiV1ScmRepositoriesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_archived_at_error_component import (
        ApiV1ScmRepositoriesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_archived_error_component import (
        ApiV1ScmRepositoriesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_archived_reason_error_component import (
        ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_credential_error_component import (
        ApiV1ScmRepositoriesCreateCredentialErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_criticality_error_component import (
        ApiV1ScmRepositoriesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_debug_mode_error_component import (
        ApiV1ScmRepositoriesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_display_name_error_component import (
        ApiV1ScmRepositoriesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_groups_count_error_component import (
        ApiV1ScmRepositoriesCreateGroupsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_hostname_error_component import (
        ApiV1ScmRepositoriesCreateHostnameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_k8s_app_error_component import (
        ApiV1ScmRepositoriesCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_k8s_cluster_error_component import (
        ApiV1ScmRepositoriesCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_kind_error_component import (
        ApiV1ScmRepositoriesCreateKindErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_labels_error_component import (
        ApiV1ScmRepositoriesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_metadata_error_component import (
        ApiV1ScmRepositoriesCreateMetadataErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_name_error_component import (
        ApiV1ScmRepositoriesCreateNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_non_field_errors_error_component import (
        ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_platform_service_error_component import (
        ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_projects_count_error_component import (
        ApiV1ScmRepositoriesCreateProjectsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_provider_error_component import (
        ApiV1ScmRepositoriesCreateProviderErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_provider_id_error_component import (
        ApiV1ScmRepositoriesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_provider_reference_error_component import (
        ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_reconciliation_enabled_error_component import (
        ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_repository_version_error_component import (
        ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_sla_availability_error_component import (
        ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_sla_target_error_component import (
        ApiV1ScmRepositoriesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_slo_availability_error_component import (
        ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_slo_target_error_component import (
        ApiV1ScmRepositoriesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_target_availability_error_component import (
        ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_tolerations_error_component import (
        ApiV1ScmRepositoriesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_create_users_count_error_component import (
        ApiV1ScmRepositoriesCreateUsersCountErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ScmRepositoriesCreateValidationError")


@_attrs_define
class ApiV1ScmRepositoriesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ScmRepositoriesCreateAnnotationsErrorComponent |
            ApiV1ScmRepositoriesCreateArchivedAtErrorComponent | ApiV1ScmRepositoriesCreateArchivedErrorComponent |
            ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent | ApiV1ScmRepositoriesCreateCredentialErrorComponent |
            ApiV1ScmRepositoriesCreateCriticalityErrorComponent | ApiV1ScmRepositoriesCreateDebugModeErrorComponent |
            ApiV1ScmRepositoriesCreateDisplayNameErrorComponent | ApiV1ScmRepositoriesCreateGroupsCountErrorComponent |
            ApiV1ScmRepositoriesCreateHostnameErrorComponent | ApiV1ScmRepositoriesCreateK8SAppErrorComponent |
            ApiV1ScmRepositoriesCreateK8SClusterErrorComponent | ApiV1ScmRepositoriesCreateKindErrorComponent |
            ApiV1ScmRepositoriesCreateLabelsErrorComponent | ApiV1ScmRepositoriesCreateMetadataErrorComponent |
            ApiV1ScmRepositoriesCreateNameErrorComponent | ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent |
            ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent | ApiV1ScmRepositoriesCreateProjectsCountErrorComponent
            | ApiV1ScmRepositoriesCreateProviderErrorComponent | ApiV1ScmRepositoriesCreateProviderIdErrorComponent |
            ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent |
            ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent |
            ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent |
            ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent | ApiV1ScmRepositoriesCreateSlaTargetErrorComponent |
            ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent | ApiV1ScmRepositoriesCreateSloTargetErrorComponent |
            ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent | ApiV1ScmRepositoriesCreateTolerationsErrorComponent
            | ApiV1ScmRepositoriesCreateUsersCountErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ScmRepositoriesCreateAnnotationsErrorComponent
        | ApiV1ScmRepositoriesCreateArchivedAtErrorComponent
        | ApiV1ScmRepositoriesCreateArchivedErrorComponent
        | ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent
        | ApiV1ScmRepositoriesCreateCredentialErrorComponent
        | ApiV1ScmRepositoriesCreateCriticalityErrorComponent
        | ApiV1ScmRepositoriesCreateDebugModeErrorComponent
        | ApiV1ScmRepositoriesCreateDisplayNameErrorComponent
        | ApiV1ScmRepositoriesCreateGroupsCountErrorComponent
        | ApiV1ScmRepositoriesCreateHostnameErrorComponent
        | ApiV1ScmRepositoriesCreateK8SAppErrorComponent
        | ApiV1ScmRepositoriesCreateK8SClusterErrorComponent
        | ApiV1ScmRepositoriesCreateKindErrorComponent
        | ApiV1ScmRepositoriesCreateLabelsErrorComponent
        | ApiV1ScmRepositoriesCreateMetadataErrorComponent
        | ApiV1ScmRepositoriesCreateNameErrorComponent
        | ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent
        | ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent
        | ApiV1ScmRepositoriesCreateProjectsCountErrorComponent
        | ApiV1ScmRepositoriesCreateProviderErrorComponent
        | ApiV1ScmRepositoriesCreateProviderIdErrorComponent
        | ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent
        | ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent
        | ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent
        | ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent
        | ApiV1ScmRepositoriesCreateSlaTargetErrorComponent
        | ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent
        | ApiV1ScmRepositoriesCreateSloTargetErrorComponent
        | ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent
        | ApiV1ScmRepositoriesCreateTolerationsErrorComponent
        | ApiV1ScmRepositoriesCreateUsersCountErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_scm_repositories_create_annotations_error_component import (
            ApiV1ScmRepositoriesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_archived_at_error_component import (
            ApiV1ScmRepositoriesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_archived_error_component import (
            ApiV1ScmRepositoriesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_archived_reason_error_component import (
            ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_credential_error_component import (
            ApiV1ScmRepositoriesCreateCredentialErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_criticality_error_component import (
            ApiV1ScmRepositoriesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_debug_mode_error_component import (
            ApiV1ScmRepositoriesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_display_name_error_component import (
            ApiV1ScmRepositoriesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_groups_count_error_component import (
            ApiV1ScmRepositoriesCreateGroupsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_hostname_error_component import (
            ApiV1ScmRepositoriesCreateHostnameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_k8s_app_error_component import (
            ApiV1ScmRepositoriesCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_kind_error_component import (
            ApiV1ScmRepositoriesCreateKindErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_labels_error_component import (
            ApiV1ScmRepositoriesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_name_error_component import (
            ApiV1ScmRepositoriesCreateNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_non_field_errors_error_component import (
            ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_platform_service_error_component import (
            ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_projects_count_error_component import (
            ApiV1ScmRepositoriesCreateProjectsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_provider_error_component import (
            ApiV1ScmRepositoriesCreateProviderErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_provider_id_error_component import (
            ApiV1ScmRepositoriesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_provider_reference_error_component import (
            ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_repository_version_error_component import (
            ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_sla_availability_error_component import (
            ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_sla_target_error_component import (
            ApiV1ScmRepositoriesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_slo_availability_error_component import (
            ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_slo_target_error_component import (
            ApiV1ScmRepositoriesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_target_availability_error_component import (
            ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_tolerations_error_component import (
            ApiV1ScmRepositoriesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_users_count_error_component import (
            ApiV1ScmRepositoriesCreateUsersCountErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateUsersCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateGroupsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesCreateCredentialErrorComponent):
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
        from ..models.api_v1_scm_repositories_create_annotations_error_component import (
            ApiV1ScmRepositoriesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_archived_at_error_component import (
            ApiV1ScmRepositoriesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_archived_error_component import (
            ApiV1ScmRepositoriesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_archived_reason_error_component import (
            ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_credential_error_component import (
            ApiV1ScmRepositoriesCreateCredentialErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_criticality_error_component import (
            ApiV1ScmRepositoriesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_debug_mode_error_component import (
            ApiV1ScmRepositoriesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_display_name_error_component import (
            ApiV1ScmRepositoriesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_groups_count_error_component import (
            ApiV1ScmRepositoriesCreateGroupsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_hostname_error_component import (
            ApiV1ScmRepositoriesCreateHostnameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_k8s_app_error_component import (
            ApiV1ScmRepositoriesCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_kind_error_component import (
            ApiV1ScmRepositoriesCreateKindErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_labels_error_component import (
            ApiV1ScmRepositoriesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_metadata_error_component import (
            ApiV1ScmRepositoriesCreateMetadataErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_name_error_component import (
            ApiV1ScmRepositoriesCreateNameErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_non_field_errors_error_component import (
            ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_platform_service_error_component import (
            ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_projects_count_error_component import (
            ApiV1ScmRepositoriesCreateProjectsCountErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_provider_error_component import (
            ApiV1ScmRepositoriesCreateProviderErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_provider_id_error_component import (
            ApiV1ScmRepositoriesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_provider_reference_error_component import (
            ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_repository_version_error_component import (
            ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_sla_availability_error_component import (
            ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_sla_target_error_component import (
            ApiV1ScmRepositoriesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_slo_availability_error_component import (
            ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_slo_target_error_component import (
            ApiV1ScmRepositoriesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_target_availability_error_component import (
            ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_tolerations_error_component import (
            ApiV1ScmRepositoriesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_scm_repositories_create_users_count_error_component import (
            ApiV1ScmRepositoriesCreateUsersCountErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ScmRepositoriesCreateAnnotationsErrorComponent
                | ApiV1ScmRepositoriesCreateArchivedAtErrorComponent
                | ApiV1ScmRepositoriesCreateArchivedErrorComponent
                | ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent
                | ApiV1ScmRepositoriesCreateCredentialErrorComponent
                | ApiV1ScmRepositoriesCreateCriticalityErrorComponent
                | ApiV1ScmRepositoriesCreateDebugModeErrorComponent
                | ApiV1ScmRepositoriesCreateDisplayNameErrorComponent
                | ApiV1ScmRepositoriesCreateGroupsCountErrorComponent
                | ApiV1ScmRepositoriesCreateHostnameErrorComponent
                | ApiV1ScmRepositoriesCreateK8SAppErrorComponent
                | ApiV1ScmRepositoriesCreateK8SClusterErrorComponent
                | ApiV1ScmRepositoriesCreateKindErrorComponent
                | ApiV1ScmRepositoriesCreateLabelsErrorComponent
                | ApiV1ScmRepositoriesCreateMetadataErrorComponent
                | ApiV1ScmRepositoriesCreateNameErrorComponent
                | ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent
                | ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent
                | ApiV1ScmRepositoriesCreateProjectsCountErrorComponent
                | ApiV1ScmRepositoriesCreateProviderErrorComponent
                | ApiV1ScmRepositoriesCreateProviderIdErrorComponent
                | ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent
                | ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent
                | ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent
                | ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent
                | ApiV1ScmRepositoriesCreateSlaTargetErrorComponent
                | ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent
                | ApiV1ScmRepositoriesCreateSloTargetErrorComponent
                | ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent
                | ApiV1ScmRepositoriesCreateTolerationsErrorComponent
                | ApiV1ScmRepositoriesCreateUsersCountErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_0 = (
                        ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_1 = (
                        ApiV1ScmRepositoriesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_2 = (
                        ApiV1ScmRepositoriesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_3 = (
                        ApiV1ScmRepositoriesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_4 = (
                        ApiV1ScmRepositoriesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_5 = (
                        ApiV1ScmRepositoriesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_6 = (
                        ApiV1ScmRepositoriesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_7 = (
                        ApiV1ScmRepositoriesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_8 = (
                        ApiV1ScmRepositoriesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_9 = (
                        ApiV1ScmRepositoriesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_10 = (
                        ApiV1ScmRepositoriesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_11 = (
                        ApiV1ScmRepositoriesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_12 = (
                        ApiV1ScmRepositoriesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_13 = (
                        ApiV1ScmRepositoriesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_14 = (
                        ApiV1ScmRepositoriesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_15 = (
                        ApiV1ScmRepositoriesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_16 = (
                        ApiV1ScmRepositoriesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_17 = (
                        ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_18 = (
                        ApiV1ScmRepositoriesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_19 = (
                        ApiV1ScmRepositoriesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_20 = (
                        ApiV1ScmRepositoriesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_21 = (
                        ApiV1ScmRepositoriesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_22 = (
                        ApiV1ScmRepositoriesCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_23 = (
                        ApiV1ScmRepositoriesCreateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_24 = (
                        ApiV1ScmRepositoriesCreateUsersCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_25 = (
                        ApiV1ScmRepositoriesCreateGroupsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_26 = (
                        ApiV1ScmRepositoriesCreateRepositoryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_27 = (
                        ApiV1ScmRepositoriesCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_28 = (
                        ApiV1ScmRepositoriesCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_create_error_type_29 = (
                        ApiV1ScmRepositoriesCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_scm_repositories_create_error_type_30 = (
                    ApiV1ScmRepositoriesCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_scm_repositories_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_scm_repositories_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_scm_repositories_create_validation_error.additional_properties = d
        return api_v1_scm_repositories_create_validation_error

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
