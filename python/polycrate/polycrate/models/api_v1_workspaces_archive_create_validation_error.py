from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_archive_create_actual_availability_error_component import (
        ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_alternative_name_error_component import (
        ApiV1WorkspacesArchiveCreateAlternativeNameErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_annotations_error_component import (
        ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_archived_at_error_component import (
        ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_archived_error_component import (
        ApiV1WorkspacesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_archived_reason_error_component import (
        ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_backup_enabled_error_component import (
        ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_criticality_error_component import (
        ApiV1WorkspacesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_debug_mode_error_component import (
        ApiV1WorkspacesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_description_error_component import (
        ApiV1WorkspacesArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_discovery_enabled_error_component import (
        ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_display_name_error_component import (
        ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_encrypted_error_component import (
        ApiV1WorkspacesArchiveCreateEncryptedErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_endpoint_monitors_error_component import (
        ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_gitlab_project_id_error_component import (
        ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_gitlab_project_url_error_component import (
        ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_global_endpoint_monitor_error_component import (
        ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_has_incompatible_kubeconfig_error_component import (
        ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_kind_error_component import (
        ApiV1WorkspacesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_labels_error_component import (
        ApiV1WorkspacesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_monitoring_workspace_allowlist_ids_error_component import (
        ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_name_error_component import (
        ApiV1WorkspacesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_non_field_errors_error_component import (
        ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_notifications_enabled_error_component import (
        ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_on_premise_error_component import (
        ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_organization_id_error_component import (
        ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_owner_id_error_component import (
        ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_platform_service_error_component import (
        ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_pop_id_error_component import (
        ApiV1WorkspacesArchiveCreatePopIdErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_provider_error_component import (
        ApiV1WorkspacesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_provider_id_error_component import (
        ApiV1WorkspacesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_provider_reference_error_component import (
        ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_purpose_error_component import (
        ApiV1WorkspacesArchiveCreatePurposeErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_readme_md_error_component import (
        ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_reconciliation_enabled_error_component import (
        ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_scope_error_component import (
        ApiV1WorkspacesArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_secrets_poly_raw_error_component import (
        ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_sla_availability_error_component import (
        ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_sla_target_error_component import (
        ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_slo_availability_error_component import (
        ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_slo_target_error_component import (
        ApiV1WorkspacesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_target_availability_error_component import (
        ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_template_error_component import (
        ApiV1WorkspacesArchiveCreateTemplateErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_urls_error_component import (
        ApiV1WorkspacesArchiveCreateUrlsErrorComponent,
    )
    from ..models.api_v1_workspaces_archive_create_workspace_inventory_raw_error_component import (
        ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent,
    )


T = TypeVar("T", bound="ApiV1WorkspacesArchiveCreateValidationError")


@_attrs_define
class ApiV1WorkspacesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent |
            ApiV1WorkspacesArchiveCreateAlternativeNameErrorComponent |
            ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent | ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent |
            ApiV1WorkspacesArchiveCreateArchivedErrorComponent | ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent |
            ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent | ApiV1WorkspacesArchiveCreateCriticalityErrorComponent
            | ApiV1WorkspacesArchiveCreateDebugModeErrorComponent | ApiV1WorkspacesArchiveCreateDescriptionErrorComponent |
            ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent | ApiV1WorkspacesArchiveCreateEncryptedErrorComponent |
            ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent |
            ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent |
            ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent |
            ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent |
            ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent |
            ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent |
            ApiV1WorkspacesArchiveCreateKindErrorComponent | ApiV1WorkspacesArchiveCreateLabelsErrorComponent |
            ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent |
            ApiV1WorkspacesArchiveCreateNameErrorComponent | ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent |
            ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent | ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent |
            ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent | ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent |
            ApiV1WorkspacesArchiveCreatePopIdErrorComponent | ApiV1WorkspacesArchiveCreateProviderErrorComponent |
            ApiV1WorkspacesArchiveCreateProviderIdErrorComponent |
            ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent | ApiV1WorkspacesArchiveCreatePurposeErrorComponent
            | ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent |
            ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1WorkspacesArchiveCreateScopeErrorComponent | ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent |
            ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent | ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent
            | ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1WorkspacesArchiveCreateSloTargetErrorComponent |
            ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1WorkspacesArchiveCreateTemplateErrorComponent | ApiV1WorkspacesArchiveCreateUrlsErrorComponent |
            ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent
        | ApiV1WorkspacesArchiveCreateAlternativeNameErrorComponent
        | ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent
        | ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent
        | ApiV1WorkspacesArchiveCreateArchivedErrorComponent
        | ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent
        | ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent
        | ApiV1WorkspacesArchiveCreateCriticalityErrorComponent
        | ApiV1WorkspacesArchiveCreateDebugModeErrorComponent
        | ApiV1WorkspacesArchiveCreateDescriptionErrorComponent
        | ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent
        | ApiV1WorkspacesArchiveCreateEncryptedErrorComponent
        | ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent
        | ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent
        | ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent
        | ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent
        | ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent
        | ApiV1WorkspacesArchiveCreateKindErrorComponent
        | ApiV1WorkspacesArchiveCreateLabelsErrorComponent
        | ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent
        | ApiV1WorkspacesArchiveCreateNameErrorComponent
        | ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent
        | ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent
        | ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent
        | ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent
        | ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent
        | ApiV1WorkspacesArchiveCreatePopIdErrorComponent
        | ApiV1WorkspacesArchiveCreateProviderErrorComponent
        | ApiV1WorkspacesArchiveCreateProviderIdErrorComponent
        | ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent
        | ApiV1WorkspacesArchiveCreatePurposeErrorComponent
        | ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent
        | ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1WorkspacesArchiveCreateScopeErrorComponent
        | ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent
        | ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent
        | ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1WorkspacesArchiveCreateSloTargetErrorComponent
        | ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1WorkspacesArchiveCreateTemplateErrorComponent
        | ApiV1WorkspacesArchiveCreateUrlsErrorComponent
        | ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_archive_create_actual_availability_error_component import (
            ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_annotations_error_component import (
            ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_archived_at_error_component import (
            ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_archived_error_component import (
            ApiV1WorkspacesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_archived_reason_error_component import (
            ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_backup_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_criticality_error_component import (
            ApiV1WorkspacesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_debug_mode_error_component import (
            ApiV1WorkspacesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_description_error_component import (
            ApiV1WorkspacesArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_discovery_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_display_name_error_component import (
            ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_encrypted_error_component import (
            ApiV1WorkspacesArchiveCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_kind_error_component import (
            ApiV1WorkspacesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_labels_error_component import (
            ApiV1WorkspacesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_name_error_component import (
            ApiV1WorkspacesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_non_field_errors_error_component import (
            ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_notifications_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_on_premise_error_component import (
            ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_organization_id_error_component import (
            ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_owner_id_error_component import (
            ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_platform_service_error_component import (
            ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_pop_id_error_component import (
            ApiV1WorkspacesArchiveCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_provider_error_component import (
            ApiV1WorkspacesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_provider_id_error_component import (
            ApiV1WorkspacesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_provider_reference_error_component import (
            ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_purpose_error_component import (
            ApiV1WorkspacesArchiveCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_readme_md_error_component import (
            ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_scope_error_component import (
            ApiV1WorkspacesArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_sla_availability_error_component import (
            ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_sla_target_error_component import (
            ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_slo_availability_error_component import (
            ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_slo_target_error_component import (
            ApiV1WorkspacesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_target_availability_error_component import (
            ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_template_error_component import (
            ApiV1WorkspacesArchiveCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_urls_error_component import (
            ApiV1WorkspacesArchiveCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateEncryptedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreatePopIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreatePurposeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent):
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
        from ..models.api_v1_workspaces_archive_create_actual_availability_error_component import (
            ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_alternative_name_error_component import (
            ApiV1WorkspacesArchiveCreateAlternativeNameErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_annotations_error_component import (
            ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_archived_at_error_component import (
            ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_archived_error_component import (
            ApiV1WorkspacesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_archived_reason_error_component import (
            ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_backup_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_criticality_error_component import (
            ApiV1WorkspacesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_debug_mode_error_component import (
            ApiV1WorkspacesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_description_error_component import (
            ApiV1WorkspacesArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_discovery_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_display_name_error_component import (
            ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_encrypted_error_component import (
            ApiV1WorkspacesArchiveCreateEncryptedErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_endpoint_monitors_error_component import (
            ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_gitlab_project_id_error_component import (
            ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_gitlab_project_url_error_component import (
            ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_global_endpoint_monitor_error_component import (
            ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_has_incompatible_kubeconfig_error_component import (
            ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_kind_error_component import (
            ApiV1WorkspacesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_labels_error_component import (
            ApiV1WorkspacesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_monitoring_workspace_allowlist_ids_error_component import (
            ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_name_error_component import (
            ApiV1WorkspacesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_non_field_errors_error_component import (
            ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_notifications_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_on_premise_error_component import (
            ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_organization_id_error_component import (
            ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_owner_id_error_component import (
            ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_platform_service_error_component import (
            ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_pop_id_error_component import (
            ApiV1WorkspacesArchiveCreatePopIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_provider_error_component import (
            ApiV1WorkspacesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_provider_id_error_component import (
            ApiV1WorkspacesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_provider_reference_error_component import (
            ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_purpose_error_component import (
            ApiV1WorkspacesArchiveCreatePurposeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_readme_md_error_component import (
            ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_reconciliation_enabled_error_component import (
            ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_scope_error_component import (
            ApiV1WorkspacesArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_secrets_poly_raw_error_component import (
            ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_sla_availability_error_component import (
            ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_sla_target_error_component import (
            ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_slo_availability_error_component import (
            ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_slo_target_error_component import (
            ApiV1WorkspacesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_target_availability_error_component import (
            ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_template_error_component import (
            ApiV1WorkspacesArchiveCreateTemplateErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_urls_error_component import (
            ApiV1WorkspacesArchiveCreateUrlsErrorComponent,
        )
        from ..models.api_v1_workspaces_archive_create_workspace_inventory_raw_error_component import (
            ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent
                | ApiV1WorkspacesArchiveCreateAlternativeNameErrorComponent
                | ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent
                | ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent
                | ApiV1WorkspacesArchiveCreateArchivedErrorComponent
                | ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent
                | ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent
                | ApiV1WorkspacesArchiveCreateCriticalityErrorComponent
                | ApiV1WorkspacesArchiveCreateDebugModeErrorComponent
                | ApiV1WorkspacesArchiveCreateDescriptionErrorComponent
                | ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent
                | ApiV1WorkspacesArchiveCreateEncryptedErrorComponent
                | ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent
                | ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent
                | ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent
                | ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent
                | ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent
                | ApiV1WorkspacesArchiveCreateKindErrorComponent
                | ApiV1WorkspacesArchiveCreateLabelsErrorComponent
                | ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent
                | ApiV1WorkspacesArchiveCreateNameErrorComponent
                | ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent
                | ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent
                | ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent
                | ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent
                | ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent
                | ApiV1WorkspacesArchiveCreatePopIdErrorComponent
                | ApiV1WorkspacesArchiveCreateProviderErrorComponent
                | ApiV1WorkspacesArchiveCreateProviderIdErrorComponent
                | ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent
                | ApiV1WorkspacesArchiveCreatePurposeErrorComponent
                | ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent
                | ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1WorkspacesArchiveCreateScopeErrorComponent
                | ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent
                | ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent
                | ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1WorkspacesArchiveCreateSloTargetErrorComponent
                | ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1WorkspacesArchiveCreateTemplateErrorComponent
                | ApiV1WorkspacesArchiveCreateUrlsErrorComponent
                | ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_0 = (
                        ApiV1WorkspacesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_1 = (
                        ApiV1WorkspacesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_2 = (
                        ApiV1WorkspacesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_3 = (
                        ApiV1WorkspacesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_4 = (
                        ApiV1WorkspacesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_5 = (
                        ApiV1WorkspacesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_6 = (
                        ApiV1WorkspacesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_7 = (
                        ApiV1WorkspacesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_8 = (
                        ApiV1WorkspacesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_9 = (
                        ApiV1WorkspacesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_10 = (
                        ApiV1WorkspacesArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_11 = (
                        ApiV1WorkspacesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_12 = (
                        ApiV1WorkspacesArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_13 = (
                        ApiV1WorkspacesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_14 = (
                        ApiV1WorkspacesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_15 = (
                        ApiV1WorkspacesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_16 = (
                        ApiV1WorkspacesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_17 = (
                        ApiV1WorkspacesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_18 = (
                        ApiV1WorkspacesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_19 = (
                        ApiV1WorkspacesArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_20 = (
                        ApiV1WorkspacesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_21 = (
                        ApiV1WorkspacesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_22 = (
                        ApiV1WorkspacesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_23 = (
                        ApiV1WorkspacesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_24 = (
                        ApiV1WorkspacesArchiveCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_25 = (
                        ApiV1WorkspacesArchiveCreateGitlabProjectUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_26 = (
                        ApiV1WorkspacesArchiveCreateOnPremiseErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_27 = (
                        ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_28 = (
                        ApiV1WorkspacesArchiveCreateGlobalEndpointMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_29 = (
                        ApiV1WorkspacesArchiveCreateMonitoringWorkspaceAllowlistIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_30 = (
                        ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_31 = (
                        ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_32 = (
                        ApiV1WorkspacesArchiveCreateHasIncompatibleKubeconfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_33 = (
                        ApiV1WorkspacesArchiveCreateEndpointMonitorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_34 = (
                        ApiV1WorkspacesArchiveCreateSecretsPolyRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_35 = (
                        ApiV1WorkspacesArchiveCreateWorkspaceInventoryRawErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_36 = (
                        ApiV1WorkspacesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_37 = (
                        ApiV1WorkspacesArchiveCreateEncryptedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_38 = (
                        ApiV1WorkspacesArchiveCreatePopIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_39 = (
                        ApiV1WorkspacesArchiveCreateTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_40 = (
                        ApiV1WorkspacesArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_41 = (
                        ApiV1WorkspacesArchiveCreatePurposeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_42 = (
                        ApiV1WorkspacesArchiveCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_43 = (
                        ApiV1WorkspacesArchiveCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_archive_create_error_type_44 = (
                        ApiV1WorkspacesArchiveCreateReadmeMdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_archive_create_error_type_45 = (
                    ApiV1WorkspacesArchiveCreateAlternativeNameErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_archive_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_archive_create_validation_error.additional_properties = d
        return api_v1_workspaces_archive_create_validation_error

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
