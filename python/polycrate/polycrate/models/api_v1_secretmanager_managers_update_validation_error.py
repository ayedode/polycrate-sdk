from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_secretmanager_managers_update_annotations_error_component import (
        ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_archived_at_error_component import (
        ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_archived_error_component import (
        ApiV1SecretmanagerManagersUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_archived_reason_error_component import (
        ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_auth_methods_count_error_component import (
        ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_credential_error_component import (
        ApiV1SecretmanagerManagersUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_criticality_error_component import (
        ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_debug_mode_error_component import (
        ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_display_name_error_component import (
        ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_hostname_error_component import (
        ApiV1SecretmanagerManagersUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_is_initialized_error_component import (
        ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_is_sealed_error_component import (
        ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_k8s_app_error_component import (
        ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_k8s_cluster_error_component import (
        ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_kind_error_component import (
        ApiV1SecretmanagerManagersUpdateKindErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_labels_error_component import (
        ApiV1SecretmanagerManagersUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_metadata_error_component import (
        ApiV1SecretmanagerManagersUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_name_error_component import (
        ApiV1SecretmanagerManagersUpdateNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_non_field_errors_error_component import (
        ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_platform_service_error_component import (
        ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_policies_count_error_component import (
        ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_provider_error_component import (
        ApiV1SecretmanagerManagersUpdateProviderErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_provider_id_error_component import (
        ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_provider_reference_error_component import (
        ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_reconciliation_enabled_error_component import (
        ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_secrets_engines_count_error_component import (
        ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_sla_availability_error_component import (
        ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_sla_target_error_component import (
        ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_slo_availability_error_component import (
        ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_slo_target_error_component import (
        ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_target_availability_error_component import (
        ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_tolerations_error_component import (
        ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_vault_mode_error_component import (
        ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_update_vault_version_error_component import (
        ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1SecretmanagerManagersUpdateValidationError")


@_attrs_define
class ApiV1SecretmanagerManagersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent |
            ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent |
            ApiV1SecretmanagerManagersUpdateArchivedErrorComponent |
            ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent |
            ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent |
            ApiV1SecretmanagerManagersUpdateCredentialErrorComponent |
            ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent |
            ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent |
            ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent |
            ApiV1SecretmanagerManagersUpdateHostnameErrorComponent |
            ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent |
            ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent | ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent |
            ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent | ApiV1SecretmanagerManagersUpdateKindErrorComponent |
            ApiV1SecretmanagerManagersUpdateLabelsErrorComponent | ApiV1SecretmanagerManagersUpdateMetadataErrorComponent |
            ApiV1SecretmanagerManagersUpdateNameErrorComponent |
            ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent |
            ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent |
            ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent |
            ApiV1SecretmanagerManagersUpdateProviderErrorComponent |
            ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent |
            ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent |
            ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent |
            ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent |
            ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent |
            ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent |
            ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent |
            ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent |
            ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent
        | ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent
        | ApiV1SecretmanagerManagersUpdateArchivedErrorComponent
        | ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent
        | ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent
        | ApiV1SecretmanagerManagersUpdateCredentialErrorComponent
        | ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent
        | ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent
        | ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent
        | ApiV1SecretmanagerManagersUpdateHostnameErrorComponent
        | ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent
        | ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent
        | ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent
        | ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent
        | ApiV1SecretmanagerManagersUpdateKindErrorComponent
        | ApiV1SecretmanagerManagersUpdateLabelsErrorComponent
        | ApiV1SecretmanagerManagersUpdateMetadataErrorComponent
        | ApiV1SecretmanagerManagersUpdateNameErrorComponent
        | ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent
        | ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent
        | ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent
        | ApiV1SecretmanagerManagersUpdateProviderErrorComponent
        | ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent
        | ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent
        | ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent
        | ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent
        | ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent
        | ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent
        | ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent
        | ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent
        | ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_secretmanager_managers_update_annotations_error_component import (
            ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_archived_at_error_component import (
            ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_archived_error_component import (
            ApiV1SecretmanagerManagersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_archived_reason_error_component import (
            ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_credential_error_component import (
            ApiV1SecretmanagerManagersUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_criticality_error_component import (
            ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_debug_mode_error_component import (
            ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_display_name_error_component import (
            ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_hostname_error_component import (
            ApiV1SecretmanagerManagersUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_is_initialized_error_component import (
            ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_is_sealed_error_component import (
            ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_k8s_app_error_component import (
            ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_kind_error_component import (
            ApiV1SecretmanagerManagersUpdateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_labels_error_component import (
            ApiV1SecretmanagerManagersUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_name_error_component import (
            ApiV1SecretmanagerManagersUpdateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_platform_service_error_component import (
            ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_policies_count_error_component import (
            ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_provider_error_component import (
            ApiV1SecretmanagerManagersUpdateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_provider_id_error_component import (
            ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_provider_reference_error_component import (
            ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_sla_availability_error_component import (
            ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_sla_target_error_component import (
            ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_slo_availability_error_component import (
            ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_slo_target_error_component import (
            ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_target_availability_error_component import (
            ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_tolerations_error_component import (
            ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_vault_mode_error_component import (
            ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_vault_version_error_component import (
            ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersUpdateCredentialErrorComponent):
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
        from ..models.api_v1_secretmanager_managers_update_annotations_error_component import (
            ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_archived_at_error_component import (
            ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_archived_error_component import (
            ApiV1SecretmanagerManagersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_archived_reason_error_component import (
            ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_credential_error_component import (
            ApiV1SecretmanagerManagersUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_criticality_error_component import (
            ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_debug_mode_error_component import (
            ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_display_name_error_component import (
            ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_hostname_error_component import (
            ApiV1SecretmanagerManagersUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_is_initialized_error_component import (
            ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_is_sealed_error_component import (
            ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_k8s_app_error_component import (
            ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_kind_error_component import (
            ApiV1SecretmanagerManagersUpdateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_labels_error_component import (
            ApiV1SecretmanagerManagersUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_metadata_error_component import (
            ApiV1SecretmanagerManagersUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_name_error_component import (
            ApiV1SecretmanagerManagersUpdateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_platform_service_error_component import (
            ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_policies_count_error_component import (
            ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_provider_error_component import (
            ApiV1SecretmanagerManagersUpdateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_provider_id_error_component import (
            ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_provider_reference_error_component import (
            ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_sla_availability_error_component import (
            ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_sla_target_error_component import (
            ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_slo_availability_error_component import (
            ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_slo_target_error_component import (
            ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_target_availability_error_component import (
            ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_tolerations_error_component import (
            ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_vault_mode_error_component import (
            ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_update_vault_version_error_component import (
            ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent
                | ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent
                | ApiV1SecretmanagerManagersUpdateArchivedErrorComponent
                | ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent
                | ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent
                | ApiV1SecretmanagerManagersUpdateCredentialErrorComponent
                | ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent
                | ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent
                | ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent
                | ApiV1SecretmanagerManagersUpdateHostnameErrorComponent
                | ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent
                | ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent
                | ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent
                | ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent
                | ApiV1SecretmanagerManagersUpdateKindErrorComponent
                | ApiV1SecretmanagerManagersUpdateLabelsErrorComponent
                | ApiV1SecretmanagerManagersUpdateMetadataErrorComponent
                | ApiV1SecretmanagerManagersUpdateNameErrorComponent
                | ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent
                | ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent
                | ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent
                | ApiV1SecretmanagerManagersUpdateProviderErrorComponent
                | ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent
                | ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent
                | ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent
                | ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent
                | ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent
                | ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent
                | ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent
                | ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent
                | ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_0 = (
                        ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_1 = (
                        ApiV1SecretmanagerManagersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_2 = (
                        ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_3 = (
                        ApiV1SecretmanagerManagersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_4 = (
                        ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_5 = (
                        ApiV1SecretmanagerManagersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_6 = (
                        ApiV1SecretmanagerManagersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_7 = (
                        ApiV1SecretmanagerManagersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_8 = (
                        ApiV1SecretmanagerManagersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_9 = (
                        ApiV1SecretmanagerManagersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_10 = (
                        ApiV1SecretmanagerManagersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_11 = (
                        ApiV1SecretmanagerManagersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_12 = (
                        ApiV1SecretmanagerManagersUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_13 = (
                        ApiV1SecretmanagerManagersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_14 = (
                        ApiV1SecretmanagerManagersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_15 = (
                        ApiV1SecretmanagerManagersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_16 = (
                        ApiV1SecretmanagerManagersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_17 = (
                        ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_18 = (
                        ApiV1SecretmanagerManagersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_19 = (
                        ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_20 = (
                        ApiV1SecretmanagerManagersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_21 = (
                        ApiV1SecretmanagerManagersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_22 = (
                        ApiV1SecretmanagerManagersUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_23 = (
                        ApiV1SecretmanagerManagersUpdateVaultModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_24 = (
                        ApiV1SecretmanagerManagersUpdateIsSealedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_25 = (
                        ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_26 = (
                        ApiV1SecretmanagerManagersUpdateSecretsEnginesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_27 = (
                        ApiV1SecretmanagerManagersUpdateAuthMethodsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_28 = (
                        ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_29 = (
                        ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_30 = (
                        ApiV1SecretmanagerManagersUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_31 = (
                        ApiV1SecretmanagerManagersUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_update_error_type_32 = (
                        ApiV1SecretmanagerManagersUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_secretmanager_managers_update_error_type_33 = (
                    ApiV1SecretmanagerManagersUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_secretmanager_managers_update_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_secretmanager_managers_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_secretmanager_managers_update_validation_error.additional_properties = d
        return api_v1_secretmanager_managers_update_validation_error

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
