from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_create_actual_availability_error_component import (
        ApiV1WorkspacesCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_create_alternative_name_error_component import (
        ApiV1WorkspacesCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_create_annotations_error_component import (
        ApiV1WorkspacesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_create_archived_at_error_component import (
        ApiV1WorkspacesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_create_archived_error_component import ApiV1WorkspacesCreateArchivedErrorComponent
    from ..models.api_v1_workspaces_create_archived_reason_error_component import (
        ApiV1WorkspacesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_create_backup_enabled_error_component import (
        ApiV1WorkspacesCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_create_criticality_error_component import (
        ApiV1WorkspacesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_create_debug_mode_error_component import (
        ApiV1WorkspacesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_create_description_error_component import (
        ApiV1WorkspacesCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_create_discovery_enabled_error_component import (
        ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_create_display_name_error_component import (
        ApiV1WorkspacesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_create_encrypted_error_component import ApiV1WorkspacesCreateEncryptedErrorComponent
    from ..models.api_v1_workspaces_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_create_kind_error_component import ApiV1WorkspacesCreateKindErrorComponent
    from ..models.api_v1_workspaces_create_labels_error_component import ApiV1WorkspacesCreateLabelsErrorComponent
    from ..models.api_v1_workspaces_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_create_name_error_component import ApiV1WorkspacesCreateNameErrorComponent
    from ..models.api_v1_workspaces_create_non_field_errors_error_component import (
        ApiV1WorkspacesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_create_notifications_enabled_error_component import (
        ApiV1WorkspacesCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_create_on_premise_error_component import (
        ApiV1WorkspacesCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_create_organization_id_error_component import (
        ApiV1WorkspacesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_create_owner_id_error_component import ApiV1WorkspacesCreateOwnerIdErrorComponent
    from ..models.api_v1_workspaces_create_platform_service_error_component import (
        ApiV1WorkspacesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_create_pop_id_error_component import ApiV1WorkspacesCreatePopIdErrorComponent
    from ..models.api_v1_workspaces_create_provider_error_component import ApiV1WorkspacesCreateProviderErrorComponent
    from ..models.api_v1_workspaces_create_provider_id_error_component import (
        ApiV1WorkspacesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_create_provider_reference_error_component import (
        ApiV1WorkspacesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_create_purpose_error_component import ApiV1WorkspacesCreatePurposeErrorComponent
    from ..models.api_v1_workspaces_create_readme_md_error_component import ApiV1WorkspacesCreateReadmeMdErrorComponent
    from ..models.api_v1_workspaces_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_create_scope_error_component import ApiV1WorkspacesCreateScopeErrorComponent
    from ..models.api_v1_workspaces_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_create_sla_availability_error_component import (
        ApiV1WorkspacesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_create_sla_target_error_component import (
        ApiV1WorkspacesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_create_slo_availability_error_component import (
        ApiV1WorkspacesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_create_slo_target_error_component import (
        ApiV1WorkspacesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_create_target_availability_error_component import (
        ApiV1WorkspacesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_create_template_error_component import ApiV1WorkspacesCreateTemplateErrorComponent
    from ..models.api_v1_workspaces_create_urls_error_component import ApiV1WorkspacesCreateUrlsErrorComponent
    from ..models.api_v1_workspaces_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesCreateValidationError")


@_attrs_define
class ApiV1WorkspacesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesCreateAlternativeNameErrorComponent | ApiV1WorkspacesCreateAnnotationsErrorComponent |
            ApiV1WorkspacesCreateArchivedAtErrorComponent | ApiV1WorkspacesCreateArchivedErrorComponent |
            ApiV1WorkspacesCreateArchivedReasonErrorComponent | ApiV1WorkspacesCreateBackupEnabledErrorComponent |
            ApiV1WorkspacesCreateCriticalityErrorComponent | ApiV1WorkspacesCreateDebugModeErrorComponent |
            ApiV1WorkspacesCreateDescriptionErrorComponent | ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesCreateDisplayNameErrorComponent | ApiV1WorkspacesCreateEncryptedErrorComponent |
            ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent | ApiV1WorkspacesCreateEndpointMonitorsErrorComponent
            | ApiV1WorkspacesCreateGitlabProjectIdErrorComponent | ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent | ApiV1WorkspacesCreateKindErrorComponent |
            ApiV1WorkspacesCreateLabelsErrorComponent | ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesCreateNameErrorComponent | ApiV1WorkspacesCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesCreateNotificationsEnabledErrorComponent | ApiV1WorkspacesCreateOnPremiseErrorComponent |
            ApiV1WorkspacesCreateOrganizationIdErrorComponent | ApiV1WorkspacesCreateOwnerIdErrorComponent |
            ApiV1WorkspacesCreatePlatformServiceErrorComponent | ApiV1WorkspacesCreatePopIdErrorComponent |
            ApiV1WorkspacesCreateProviderErrorComponent | ApiV1WorkspacesCreateProviderIdErrorComponent |
            ApiV1WorkspacesCreateProviderReferenceErrorComponent | ApiV1WorkspacesCreatePurposeErrorComponent |
            ApiV1WorkspacesCreateReadmeMdErrorComponent | ApiV1WorkspacesCreateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesCreateScopeErrorComponent | ApiV1WorkspacesCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesCreateSlaAvailabilityErrorComponent | ApiV1WorkspacesCreateSlaTargetErrorComponent |
            ApiV1WorkspacesCreateSloAvailabilityErrorComponent | ApiV1WorkspacesCreateSloTargetErrorComponent |
            ApiV1WorkspacesCreateTargetAvailabilityErrorComponent | ApiV1WorkspacesCreateTemplateErrorComponent |
            ApiV1WorkspacesCreateUrlsErrorComponent | ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesCreateAnnotationsErrorComponent
        | ApiV1WorkspacesCreateArchivedAtErrorComponent
        | ApiV1WorkspacesCreateArchivedErrorComponent
        | ApiV1WorkspacesCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesCreateCriticalityErrorComponent
        | ApiV1WorkspacesCreateDebugModeErrorComponent
        | ApiV1WorkspacesCreateDescriptionErrorComponent
        | ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesCreateDisplayNameErrorComponent
        | ApiV1WorkspacesCreateEncryptedErrorComponent
        | ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesCreateKindErrorComponent
        | ApiV1WorkspacesCreateLabelsErrorComponent
        | ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesCreateNameErrorComponent
        | ApiV1WorkspacesCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesCreateOnPremiseErrorComponent
        | ApiV1WorkspacesCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesCreateOwnerIdErrorComponent
        | ApiV1WorkspacesCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesCreatePopIdErrorComponent
        | ApiV1WorkspacesCreateProviderErrorComponent
        | ApiV1WorkspacesCreateProviderIdErrorComponent
        | ApiV1WorkspacesCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesCreatePurposeErrorComponent
        | ApiV1WorkspacesCreateReadmeMdErrorComponent
        | ApiV1WorkspacesCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesCreateScopeErrorComponent
        | ApiV1WorkspacesCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesCreateSlaTargetErrorComponent
        | ApiV1WorkspacesCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesCreateSloTargetErrorComponent
        | ApiV1WorkspacesCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesCreateTemplateErrorComponent
        | ApiV1WorkspacesCreateUrlsErrorComponent
        | ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_create_actual_availability_error_component import (
            ApiV1WorkspacesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_annotations_error_component import (
            ApiV1WorkspacesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_archived_at_error_component import (
            ApiV1WorkspacesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_create_archived_error_component import (
            ApiV1WorkspacesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_create_archived_reason_error_component import (
            ApiV1WorkspacesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_create_backup_enabled_error_component import (
            ApiV1WorkspacesCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_criticality_error_component import (
            ApiV1WorkspacesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_debug_mode_error_component import (
            ApiV1WorkspacesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_create_description_error_component import (
            ApiV1WorkspacesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_create_discovery_enabled_error_component import (
            ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_display_name_error_component import (
            ApiV1WorkspacesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_create_encrypted_error_component import (
            ApiV1WorkspacesCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_create_kind_error_component import ApiV1WorkspacesCreateKindErrorComponent
        from ..models.api_v1_workspaces_create_labels_error_component import ApiV1WorkspacesCreateLabelsErrorComponent
        from ..models.api_v1_workspaces_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_name_error_component import ApiV1WorkspacesCreateNameErrorComponent
        from ..models.api_v1_workspaces_create_non_field_errors_error_component import (
            ApiV1WorkspacesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_notifications_enabled_error_component import (
            ApiV1WorkspacesCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_on_premise_error_component import (
            ApiV1WorkspacesCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_create_organization_id_error_component import (
            ApiV1WorkspacesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_owner_id_error_component import (
            ApiV1WorkspacesCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_platform_service_error_component import (
            ApiV1WorkspacesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_create_pop_id_error_component import ApiV1WorkspacesCreatePopIdErrorComponent
        from ..models.api_v1_workspaces_create_provider_error_component import (
            ApiV1WorkspacesCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_create_provider_id_error_component import (
            ApiV1WorkspacesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_provider_reference_error_component import (
            ApiV1WorkspacesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_create_purpose_error_component import ApiV1WorkspacesCreatePurposeErrorComponent
        from ..models.api_v1_workspaces_create_readme_md_error_component import (
            ApiV1WorkspacesCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_scope_error_component import ApiV1WorkspacesCreateScopeErrorComponent
        from ..models.api_v1_workspaces_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_create_sla_availability_error_component import (
            ApiV1WorkspacesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_sla_target_error_component import (
            ApiV1WorkspacesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_create_slo_availability_error_component import (
            ApiV1WorkspacesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_slo_target_error_component import (
            ApiV1WorkspacesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_create_target_availability_error_component import (
            ApiV1WorkspacesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_template_error_component import (
            ApiV1WorkspacesCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_create_urls_error_component import ApiV1WorkspacesCreateUrlsErrorComponent
        from ..models.api_v1_workspaces_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_create_actual_availability_error_component import (
            ApiV1WorkspacesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_alternative_name_error_component import (
            ApiV1WorkspacesCreateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_create_annotations_error_component import (
            ApiV1WorkspacesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_archived_at_error_component import (
            ApiV1WorkspacesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_create_archived_error_component import (
            ApiV1WorkspacesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_create_archived_reason_error_component import (
            ApiV1WorkspacesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_create_backup_enabled_error_component import (
            ApiV1WorkspacesCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_criticality_error_component import (
            ApiV1WorkspacesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_debug_mode_error_component import (
            ApiV1WorkspacesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_create_description_error_component import (
            ApiV1WorkspacesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_create_discovery_enabled_error_component import (
            ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_display_name_error_component import (
            ApiV1WorkspacesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_create_encrypted_error_component import (
            ApiV1WorkspacesCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_create_kind_error_component import ApiV1WorkspacesCreateKindErrorComponent
        from ..models.api_v1_workspaces_create_labels_error_component import ApiV1WorkspacesCreateLabelsErrorComponent
        from ..models.api_v1_workspaces_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_name_error_component import ApiV1WorkspacesCreateNameErrorComponent
        from ..models.api_v1_workspaces_create_non_field_errors_error_component import (
            ApiV1WorkspacesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_create_notifications_enabled_error_component import (
            ApiV1WorkspacesCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_on_premise_error_component import (
            ApiV1WorkspacesCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_create_organization_id_error_component import (
            ApiV1WorkspacesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_owner_id_error_component import (
            ApiV1WorkspacesCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_platform_service_error_component import (
            ApiV1WorkspacesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_create_pop_id_error_component import ApiV1WorkspacesCreatePopIdErrorComponent
        from ..models.api_v1_workspaces_create_provider_error_component import (
            ApiV1WorkspacesCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_create_provider_id_error_component import (
            ApiV1WorkspacesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_provider_reference_error_component import (
            ApiV1WorkspacesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_create_purpose_error_component import ApiV1WorkspacesCreatePurposeErrorComponent
        from ..models.api_v1_workspaces_create_readme_md_error_component import (
            ApiV1WorkspacesCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_create_scope_error_component import ApiV1WorkspacesCreateScopeErrorComponent
        from ..models.api_v1_workspaces_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_create_sla_availability_error_component import (
            ApiV1WorkspacesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_sla_target_error_component import (
            ApiV1WorkspacesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_create_slo_availability_error_component import (
            ApiV1WorkspacesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_slo_target_error_component import (
            ApiV1WorkspacesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_create_target_availability_error_component import (
            ApiV1WorkspacesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_create_template_error_component import (
            ApiV1WorkspacesCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_create_urls_error_component import ApiV1WorkspacesCreateUrlsErrorComponent
        from ..models.api_v1_workspaces_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesCreateAnnotationsErrorComponent
                | ApiV1WorkspacesCreateArchivedAtErrorComponent
                | ApiV1WorkspacesCreateArchivedErrorComponent
                | ApiV1WorkspacesCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesCreateCriticalityErrorComponent
                | ApiV1WorkspacesCreateDebugModeErrorComponent
                | ApiV1WorkspacesCreateDescriptionErrorComponent
                | ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesCreateDisplayNameErrorComponent
                | ApiV1WorkspacesCreateEncryptedErrorComponent
                | ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesCreateKindErrorComponent
                | ApiV1WorkspacesCreateLabelsErrorComponent
                | ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesCreateNameErrorComponent
                | ApiV1WorkspacesCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesCreateOnPremiseErrorComponent
                | ApiV1WorkspacesCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesCreateOwnerIdErrorComponent
                | ApiV1WorkspacesCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesCreatePopIdErrorComponent
                | ApiV1WorkspacesCreateProviderErrorComponent
                | ApiV1WorkspacesCreateProviderIdErrorComponent
                | ApiV1WorkspacesCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesCreatePurposeErrorComponent
                | ApiV1WorkspacesCreateReadmeMdErrorComponent
                | ApiV1WorkspacesCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesCreateScopeErrorComponent
                | ApiV1WorkspacesCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesCreateSlaTargetErrorComponent
                | ApiV1WorkspacesCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesCreateSloTargetErrorComponent
                | ApiV1WorkspacesCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesCreateTemplateErrorComponent
                | ApiV1WorkspacesCreateUrlsErrorComponent
                | ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_0 = (
                        ApiV1WorkspacesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_1 = (
                        ApiV1WorkspacesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_2 = (
                        ApiV1WorkspacesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_3 = (
                        ApiV1WorkspacesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_4 = (
                        ApiV1WorkspacesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_5 = (
                        ApiV1WorkspacesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_6 = (
                        ApiV1WorkspacesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_7 = (
                        ApiV1WorkspacesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_8 = (
                        ApiV1WorkspacesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_9 = (
                        ApiV1WorkspacesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_10 = (
                        ApiV1WorkspacesCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_11 = (
                        ApiV1WorkspacesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_12 = (
                        ApiV1WorkspacesCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_13 = (
                        ApiV1WorkspacesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_14 = (
                        ApiV1WorkspacesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_15 = (
                        ApiV1WorkspacesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_16 = (
                        ApiV1WorkspacesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_17 = (
                        ApiV1WorkspacesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_18 = (
                        ApiV1WorkspacesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_19 = (
                        ApiV1WorkspacesCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_20 = (
                        ApiV1WorkspacesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_21 = (
                        ApiV1WorkspacesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_22 = (
                        ApiV1WorkspacesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_23 = (
                        ApiV1WorkspacesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_24 = (
                        ApiV1WorkspacesCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_25 = (
                        ApiV1WorkspacesCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_26 = (
                        ApiV1WorkspacesCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_27 = (
                        ApiV1WorkspacesCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_28 = (
                        ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_29 = (
                        ApiV1WorkspacesCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_30 = (
                        ApiV1WorkspacesCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_31 = (
                        ApiV1WorkspacesCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_32 = (
                        ApiV1WorkspacesCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_33 = (
                        ApiV1WorkspacesCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_34 = (
                        ApiV1WorkspacesCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_35 = (
                        ApiV1WorkspacesCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_36 = (
                        ApiV1WorkspacesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_37 = (
                        ApiV1WorkspacesCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_38 = (
                        ApiV1WorkspacesCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_39 = (
                        ApiV1WorkspacesCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_40 = (
                        ApiV1WorkspacesCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_41 = (
                        ApiV1WorkspacesCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_42 = (
                        ApiV1WorkspacesCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_43 = (
                        ApiV1WorkspacesCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_create_error_type_44 = (
                        ApiV1WorkspacesCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_create_error_type_45 = (
                    ApiV1WorkspacesCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_create_validation_error.additional_properties = d
        return api_v1_workspaces_create_validation_error

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
