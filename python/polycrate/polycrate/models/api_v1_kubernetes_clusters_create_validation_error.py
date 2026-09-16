from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_create_active_error_component import (
        ApiV1KubernetesClustersCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_actual_availability_error_component import (
        ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_addons_error_component import (
        ApiV1KubernetesClustersCreateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_alias_error_component import (
        ApiV1KubernetesClustersCreateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_annotations_error_component import (
        ApiV1KubernetesClustersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_archived_at_error_component import (
        ApiV1KubernetesClustersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_archived_error_component import (
        ApiV1KubernetesClustersCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_archived_reason_error_component import (
        ApiV1KubernetesClustersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_backup_schedules_error_component import (
        ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_baserow_id_error_component import (
        ApiV1KubernetesClustersCreateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_credential_error_component import (
        ApiV1KubernetesClustersCreateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_criticality_error_component import (
        ApiV1KubernetesClustersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_debug_mode_error_component import (
        ApiV1KubernetesClustersCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_description_error_component import (
        ApiV1KubernetesClustersCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_discovery_enabled_error_component import (
        ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_display_name_error_component import (
        ApiV1KubernetesClustersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_installed_error_component import (
        ApiV1KubernetesClustersCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_is_host_cluster_error_component import (
        ApiV1KubernetesClustersCreateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_kind_error_component import (
        ApiV1KubernetesClustersCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_kubernetes_version_error_component import (
        ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_labels_error_component import (
        ApiV1KubernetesClustersCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_last_backup_import_error_component import (
        ApiV1KubernetesClustersCreateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_name_error_component import (
        ApiV1KubernetesClustersCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_non_field_errors_error_component import (
        ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_operator_loglevel_error_component import (
        ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_platform_service_error_component import (
        ApiV1KubernetesClustersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_provider_error_component import (
        ApiV1KubernetesClustersCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_provider_id_error_component import (
        ApiV1KubernetesClustersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_provider_reference_error_component import (
        ApiV1KubernetesClustersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_scope_error_component import (
        ApiV1KubernetesClustersCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_sla_availability_error_component import (
        ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_sla_target_error_component import (
        ApiV1KubernetesClustersCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_slo_availability_error_component import (
        ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_slo_target_error_component import (
        ApiV1KubernetesClustersCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_slug_error_component import (
        ApiV1KubernetesClustersCreateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_create_target_availability_error_component import (
        ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersCreateValidationError")


@_attrs_define
class ApiV1KubernetesClustersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersCreateActiveErrorComponent |
            ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersCreateAddonsErrorComponent | ApiV1KubernetesClustersCreateAliasErrorComponent |
            ApiV1KubernetesClustersCreateAnnotationsErrorComponent |
            ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersCreateArchivedAtErrorComponent | ApiV1KubernetesClustersCreateArchivedErrorComponent |
            ApiV1KubernetesClustersCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersCreateBaserowIdErrorComponent | ApiV1KubernetesClustersCreateCredentialErrorComponent |
            ApiV1KubernetesClustersCreateCriticalityErrorComponent | ApiV1KubernetesClustersCreateDebugModeErrorComponent |
            ApiV1KubernetesClustersCreateDescriptionErrorComponent |
            ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersCreateDisplayNameErrorComponent |
            ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersCreateInstalledErrorComponent | ApiV1KubernetesClustersCreateIsHostClusterErrorComponent
            | ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersCreateKindErrorComponent |
            ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent | ApiV1KubernetesClustersCreateLabelsErrorComponent
            | ApiV1KubernetesClustersCreateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersCreateManagedByObjectIdErrorComponent | ApiV1KubernetesClustersCreateNameErrorComponent |
            ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersCreatePlatformServiceErrorComponent | ApiV1KubernetesClustersCreateProviderErrorComponent
            | ApiV1KubernetesClustersCreateProviderIdErrorComponent |
            ApiV1KubernetesClustersCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersCreateScopeErrorComponent | ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersCreateSlaTargetErrorComponent |
            ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersCreateSloTargetErrorComponent | ApiV1KubernetesClustersCreateSlugErrorComponent |
            ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersCreateActiveErrorComponent
        | ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersCreateAddonsErrorComponent
        | ApiV1KubernetesClustersCreateAliasErrorComponent
        | ApiV1KubernetesClustersCreateAnnotationsErrorComponent
        | ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersCreateArchivedAtErrorComponent
        | ApiV1KubernetesClustersCreateArchivedErrorComponent
        | ApiV1KubernetesClustersCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersCreateBaserowIdErrorComponent
        | ApiV1KubernetesClustersCreateCredentialErrorComponent
        | ApiV1KubernetesClustersCreateCriticalityErrorComponent
        | ApiV1KubernetesClustersCreateDebugModeErrorComponent
        | ApiV1KubernetesClustersCreateDescriptionErrorComponent
        | ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersCreateDisplayNameErrorComponent
        | ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersCreateInstalledErrorComponent
        | ApiV1KubernetesClustersCreateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersCreateKindErrorComponent
        | ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersCreateLabelsErrorComponent
        | ApiV1KubernetesClustersCreateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersCreateNameErrorComponent
        | ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersCreateProviderErrorComponent
        | ApiV1KubernetesClustersCreateProviderIdErrorComponent
        | ApiV1KubernetesClustersCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersCreateScopeErrorComponent
        | ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersCreateSlaTargetErrorComponent
        | ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersCreateSloTargetErrorComponent
        | ApiV1KubernetesClustersCreateSlugErrorComponent
        | ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_create_active_error_component import (
            ApiV1KubernetesClustersCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_actual_availability_error_component import (
            ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_addons_error_component import (
            ApiV1KubernetesClustersCreateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_alias_error_component import (
            ApiV1KubernetesClustersCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_annotations_error_component import (
            ApiV1KubernetesClustersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_archived_at_error_component import (
            ApiV1KubernetesClustersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_archived_error_component import (
            ApiV1KubernetesClustersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_archived_reason_error_component import (
            ApiV1KubernetesClustersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_baserow_id_error_component import (
            ApiV1KubernetesClustersCreateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_credential_error_component import (
            ApiV1KubernetesClustersCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_criticality_error_component import (
            ApiV1KubernetesClustersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_debug_mode_error_component import (
            ApiV1KubernetesClustersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_description_error_component import (
            ApiV1KubernetesClustersCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_display_name_error_component import (
            ApiV1KubernetesClustersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_installed_error_component import (
            ApiV1KubernetesClustersCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersCreateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kind_error_component import (
            ApiV1KubernetesClustersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_labels_error_component import (
            ApiV1KubernetesClustersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersCreateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_name_error_component import (
            ApiV1KubernetesClustersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_platform_service_error_component import (
            ApiV1KubernetesClustersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_provider_error_component import (
            ApiV1KubernetesClustersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_provider_id_error_component import (
            ApiV1KubernetesClustersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_provider_reference_error_component import (
            ApiV1KubernetesClustersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_scope_error_component import (
            ApiV1KubernetesClustersCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_sla_availability_error_component import (
            ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_sla_target_error_component import (
            ApiV1KubernetesClustersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_slo_availability_error_component import (
            ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_slo_target_error_component import (
            ApiV1KubernetesClustersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_slug_error_component import (
            ApiV1KubernetesClustersCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_target_availability_error_component import (
            ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_create_active_error_component import (
            ApiV1KubernetesClustersCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_actual_availability_error_component import (
            ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_addons_error_component import (
            ApiV1KubernetesClustersCreateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_alias_error_component import (
            ApiV1KubernetesClustersCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_annotations_error_component import (
            ApiV1KubernetesClustersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_archived_at_error_component import (
            ApiV1KubernetesClustersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_archived_error_component import (
            ApiV1KubernetesClustersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_archived_reason_error_component import (
            ApiV1KubernetesClustersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_baserow_id_error_component import (
            ApiV1KubernetesClustersCreateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_credential_error_component import (
            ApiV1KubernetesClustersCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_criticality_error_component import (
            ApiV1KubernetesClustersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_debug_mode_error_component import (
            ApiV1KubernetesClustersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_description_error_component import (
            ApiV1KubernetesClustersCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_display_name_error_component import (
            ApiV1KubernetesClustersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_installed_error_component import (
            ApiV1KubernetesClustersCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersCreateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kind_error_component import (
            ApiV1KubernetesClustersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_labels_error_component import (
            ApiV1KubernetesClustersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersCreateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_name_error_component import (
            ApiV1KubernetesClustersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_platform_service_error_component import (
            ApiV1KubernetesClustersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_provider_error_component import (
            ApiV1KubernetesClustersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_provider_id_error_component import (
            ApiV1KubernetesClustersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_provider_reference_error_component import (
            ApiV1KubernetesClustersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_scope_error_component import (
            ApiV1KubernetesClustersCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_sla_availability_error_component import (
            ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_sla_target_error_component import (
            ApiV1KubernetesClustersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_slo_availability_error_component import (
            ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_slo_target_error_component import (
            ApiV1KubernetesClustersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_slug_error_component import (
            ApiV1KubernetesClustersCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_create_target_availability_error_component import (
            ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersCreateActiveErrorComponent
                | ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersCreateAddonsErrorComponent
                | ApiV1KubernetesClustersCreateAliasErrorComponent
                | ApiV1KubernetesClustersCreateAnnotationsErrorComponent
                | ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersCreateArchivedAtErrorComponent
                | ApiV1KubernetesClustersCreateArchivedErrorComponent
                | ApiV1KubernetesClustersCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersCreateBaserowIdErrorComponent
                | ApiV1KubernetesClustersCreateCredentialErrorComponent
                | ApiV1KubernetesClustersCreateCriticalityErrorComponent
                | ApiV1KubernetesClustersCreateDebugModeErrorComponent
                | ApiV1KubernetesClustersCreateDescriptionErrorComponent
                | ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersCreateDisplayNameErrorComponent
                | ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersCreateInstalledErrorComponent
                | ApiV1KubernetesClustersCreateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersCreateKindErrorComponent
                | ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersCreateLabelsErrorComponent
                | ApiV1KubernetesClustersCreateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersCreateNameErrorComponent
                | ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersCreateProviderErrorComponent
                | ApiV1KubernetesClustersCreateProviderIdErrorComponent
                | ApiV1KubernetesClustersCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersCreateScopeErrorComponent
                | ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersCreateSlaTargetErrorComponent
                | ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersCreateSloTargetErrorComponent
                | ApiV1KubernetesClustersCreateSlugErrorComponent
                | ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_0 = (
                        ApiV1KubernetesClustersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_1 = (
                        ApiV1KubernetesClustersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_2 = (
                        ApiV1KubernetesClustersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_3 = (
                        ApiV1KubernetesClustersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_4 = (
                        ApiV1KubernetesClustersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_5 = (
                        ApiV1KubernetesClustersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_6 = (
                        ApiV1KubernetesClustersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_7 = (
                        ApiV1KubernetesClustersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_8 = (
                        ApiV1KubernetesClustersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_9 = (
                        ApiV1KubernetesClustersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_10 = (
                        ApiV1KubernetesClustersCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_11 = (
                        ApiV1KubernetesClustersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_12 = (
                        ApiV1KubernetesClustersCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_13 = (
                        ApiV1KubernetesClustersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_14 = (
                        ApiV1KubernetesClustersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_15 = (
                        ApiV1KubernetesClustersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_16 = (
                        ApiV1KubernetesClustersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_17 = (
                        ApiV1KubernetesClustersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_18 = (
                        ApiV1KubernetesClustersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_19 = (
                        ApiV1KubernetesClustersCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_20 = (
                        ApiV1KubernetesClustersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_21 = (
                        ApiV1KubernetesClustersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_22 = (
                        ApiV1KubernetesClustersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_23 = (
                        ApiV1KubernetesClustersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_24 = (
                        ApiV1KubernetesClustersCreateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_25 = (
                        ApiV1KubernetesClustersCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_26 = (
                        ApiV1KubernetesClustersCreateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_27 = (
                        ApiV1KubernetesClustersCreateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_28 = (
                        ApiV1KubernetesClustersCreateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_29 = (
                        ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_30 = (
                        ApiV1KubernetesClustersCreateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_31 = (
                        ApiV1KubernetesClustersCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_32 = (
                        ApiV1KubernetesClustersCreateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_33 = (
                        ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_34 = (
                        ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_35 = (
                        ApiV1KubernetesClustersCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_36 = (
                        ApiV1KubernetesClustersCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_37 = (
                        ApiV1KubernetesClustersCreateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_38 = (
                        ApiV1KubernetesClustersCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_39 = (
                        ApiV1KubernetesClustersCreateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_40 = (
                        ApiV1KubernetesClustersCreateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_41 = (
                        ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_42 = (
                        ApiV1KubernetesClustersCreateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_43 = (
                        ApiV1KubernetesClustersCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_44 = (
                        ApiV1KubernetesClustersCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_create_error_type_45 = (
                        ApiV1KubernetesClustersCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_create_error_type_46 = (
                    ApiV1KubernetesClustersCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_create_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_create_validation_error

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
